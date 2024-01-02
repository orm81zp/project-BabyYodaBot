import time
import re
import sys
import inspect
import difflib
from random import choice
from rich.console import Console
from collections import defaultdict
from baby_yoda_bot.models.context import Context
from baby_yoda_bot.utils import request_input, parse_input
from baby_yoda_bot.exceptions.exceptions import ValidationValueException
from baby_yoda_bot.commands.commands import (
    EXIT_COMMANDS,
    ARG_NAME,
    ARG_OLD_PHONE,
    ARG_PHONE,
)


class BasicBot:
    __COMMANDS_HANDLERS = {}
    __COMMANDS_METADATA__ = defaultdict(dict)
    __WIZARD_CLOSE_COMMAND = "--exit"

    @property
    def commands(self):
        """Getter, returns all commands collected by a command decorator."""

        commands = list(BasicBot.__COMMANDS_HANDLERS.keys())
        commands.extend(EXIT_COMMANDS)

        return commands

    @staticmethod
    def command(name):
        """Decorator, used to collect all commands."""

        def decorator(func):
            inner, key = BasicBot.__make_inner(func)
            BasicBot.__COMMANDS_HANDLERS[name] = func
            BasicBot.__COMMANDS_METADATA__[key]["command"] = name

            return inner

        return decorator

    @staticmethod
    def questions(args):
        """Decorator, used to collect all fields / arguments for a command."""

        def decorator(func):
            inner, key = BasicBot.__make_inner(func)
            BasicBot.__COMMANDS_METADATA__[key]["questions"] = args
            return inner

        return decorator

    @staticmethod
    def description(description):
        """Decorator, used to collect all command descriptions."""

        def decorator(func):
            inner, key = BasicBot.__make_inner(func)
            BasicBot.__COMMANDS_METADATA__[key]["description"] = description
            return inner

        return decorator

    @staticmethod
    def __make_inner(func):
        inner = func
        name = func.__name__

        if hasattr(func, "__bot_cmd__"):
            name = func.__bot_cmd__
        else:
            setattr(inner, "__bot_cmd__", name)

        return inner, name

    def __init__(self):
        self.context = Context()

    def save(self):
        """Calls contact book and notes methods to save the current state of data."""
        self.context.address_book.save_to_file()
        self.context.notes.save_to_file()

    def get_command(self):
        """Gets data from the user, parses it to find the command, and returns it."""
        user_input = request_input("Enter a command: ", self.commands)
        command = parse_input(user_input)
        return command

    def ask_command(self):
        """Prints a random message asking for a command."""
        phrases = [
            'Please, say something... Type "help" to see a hint.',
            'Sorry, I don\'t understand you! Say something! Type "help" to see a hint.',
            'I need more information, I can\'t guess. Type "help" to see a hint.',
            'You must be joking, you didn\'t say anything. Type "help" to see a hint.',
        ]
        print(choice(phrases))

    def command_not_found(self, cmd):
        """Checks if a command exists and prints a close suggestion if not."""
        if cmd not in self.__COMMANDS_HANDLERS:
            matches = difflib.get_close_matches(cmd, self.commands, n=1, cutoff=0.6)

            if matches:
                print(
                    f'"{cmd}" is not a command. The most similar one is "{matches[0]}".'
                )
            else:
                print(f'"{cmd}" is not a command. Type "help" to see a hint.')
            return True

    def exec(self, command):
        """Gets the command arguments, if necessary, and calls the command function with them."""
        if self.command_not_found(command):
            return

        executor_args = []
        executor = BasicBot.__COMMANDS_HANDLERS[command]
        metadata_key = executor.__bot_cmd__
        metadata = BasicBot.__COMMANDS_METADATA__[metadata_key]
        console = Console()
        executor_args.append(self.context)

        if "questions" in metadata:
            phrases = [
                "I'm collect your data for analysis...",
                "I will ask you a few questions.",
                "Answer a few questions to continue.",
                "I need more information to continue.",
            ]
            validated_args = []
            phrase = choice(phrases)
            console.print(
                f":mage: {phrase}\nTell me [bold]{self.__WIZARD_CLOSE_COMMAND}[/] to stop!"
            )
            history = {"name": ""}
            for rule in metadata["questions"]:
                is_optional = not rule["required"] if "required" in rule else False
                is_unique = "unique" in rule and rule["unique"]
                is_separated_list = "separated_list" in rule and rule["separated_list"]
                is_pattern = (
                    "pattern" in rule and rule["pattern"] and "pattern_error" in rule
                )

                requirements = []

                if is_unique:
                    requirements.append("unique")

                name = f'[{rule["name"]}]' if is_optional else f'<{rule["name"]}>'

                while True:
                    hint = (
                        f" ({', '.join(requirements)})" if len(requirements) > 0 else ""
                    )

                    compeltions = []
                    if rule["name"] == ARG_NAME:
                        compeltions = self.context.address_book.get_names()
                    elif rule["name"] in [ARG_OLD_PHONE, ARG_PHONE] and history["name"]:
                        contact = self.context.address_book.find_one(history["name"])
                        if contact:
                            compeltions = contact.get_list_of_phones()

                    value = request_input(f"Enter {name}{hint}: ", compeltions)
                    value = value.strip()

                    if not value and is_optional:
                        value = None
                        break

                    if value == self.__WIZARD_CLOSE_COMMAND:
                        print()
                        return

                    if rule["name"] == ARG_NAME:
                        history["name"] = value

                    if is_unique:
                        record = self.context.address_book.find_one(value)

                        if record:
                            print(f"{rule['name']} '{value}' must be unique")
                            continue

                    if is_pattern:
                        if value and not re.match(rule["pattern"], value):
                            console.print(
                                f'[red]Validation failed: {rule["pattern_error"]}[/]'
                            )
                            continue

                    if "type" in rule:
                        try:
                            if is_separated_list:
                                values = (
                                    value.split(",")
                                    if "," in value
                                    else value.split(" ")
                                )
                                value = list(
                                    map((lambda x: rule["type"](x.strip())), values)
                                )
                            else:
                                value = rule["type"](value)
                            break
                        except ValidationValueException as e:
                            console.print(f"[red]Validation failed: {e}[/]")
                            continue

                validated_args.append(value)
            executor_args.append(validated_args)

        required_args = inspect.getfullargspec(executor).args

        if len(required_args) == 2 and len(executor_args) == 1:
            executor_args.append([])

        return executor(*executor_args)

    def animate(self, data, delay=0.04):
        """Prints a row of data line by line with a delay."""
        if not ("--silent" in sys.argv or "-s" in sys.argv):
            rows = data.split("\n")

            for row in rows:
                print(row)
                time.sleep(delay)

    def listen(self):
        """Entry point for starting a Bot process."""
        print("listen method must be implemented by a children class")


__all__ = ["BasicBot"]
