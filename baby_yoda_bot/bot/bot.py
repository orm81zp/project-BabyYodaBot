import time
import sys
import inspect
import difflib
from rich.console import Console
from collections import defaultdict
from baby_yoda_bot.models.context import Context
from baby_yoda_bot.constants import TEXT
from baby_yoda_bot.utils import request_input, parse_input
from baby_yoda_bot.exceptions.exceptions import ValidationValueException
from baby_yoda_bot.commands.commands import (
    EXIT_COMMANDS,
    ARGUMENT_TYPES,
    VALIDATION_RULES,
    ARG_NAME,
)
from ..assets import logo, phrase


class Bot:
    __COMMANDS_HANDLERS = {}
    __COMMANDS_METADATA__ = defaultdict(dict)

    __INTERNAL_COMMANDS = {
        "help": "help",
        "save": "save",
    }

    __WIZARD_CLOSE_COMMAND = "#exit"

    @property
    def __commands(self):
        commands = list(Bot.__COMMANDS_HANDLERS.keys())
        commands.extend(self.__INTERNAL_COMMANDS.values())
        commands.extend(EXIT_COMMANDS)

        return commands

    @staticmethod
    def command(name):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_HANDLERS[name] = func
            Bot.__COMMANDS_METADATA__[key]["command"] = name

            return inner

        return decorator

    @staticmethod
    def questions(args):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__[key]["questions"] = args

            return inner

        return decorator

    @staticmethod
    def description(description):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__[key]["description"] = description

            return inner

        return decorator

    @staticmethod
    def rules(rules):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__[key]["rules"] = rules

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

    def __exec(self, command):
        executor_args = [self.context]
        executor = Bot.__COMMANDS_HANDLERS[command]
        metadata_key = executor.__bot_cmd__
        metadata = Bot.__COMMANDS_METADATA__[metadata_key]
        console = Console()

        if "questions" in metadata:
            validated_args = []
            console.print(
                f":mage: I'm collecting your data...\n(Say {self.__WIZARD_CLOSE_COMMAND} to stop)"
            )

            for rule in metadata["questions"]:
                is_optional = not rule["required"] if "required" in rule else False
                is_unique = "unique" in rule and rule["unique"]

                requirements = []

                if is_optional:
                    requirements.append("optional")

                if is_unique:
                    requirements.append("unique")

                while True:
                    hint = (
                        f" ({', '.join(requirements)})" if len(requirements) > 0 else ""
                    )

                    compeltions = []
                    if rule["name"] == ARG_NAME:
                        compeltions = self.context.address_book.get_names()
                    value = request_input(
                        f'Enter {rule["name"].capitalize()}{hint}: ', compeltions
                    )

                    if value.strip() == self.__WIZARD_CLOSE_COMMAND:
                        print("\n")
                        return

                    if not value and is_optional:
                        value = None
                        break

                    value = value.strip()

                    if is_unique:
                        record = self.context.address_book.find_one(value)

                        if record:
                            print(f"{rule['name']} '{value}' must be unique")
                            continue

                    if "type" in rule:
                        try:
                            value = rule["type"](value)
                            break
                        except ValidationValueException as e:
                            print(e)
                            continue
                if value:
                    validated_args.append(value)
            executor_args.append(validated_args)

        required_args = inspect.getfullargspec(executor).args

        if len(required_args) == 2 and len(executor_args) == 1:
            executor_args.append([])

        return executor(*executor_args)

    @staticmethod
    def help():
        commands_output = ""
        all_arguments = {}
        for commands_metadata in Bot.__COMMANDS_METADATA__.values():
            description = "no description"
            command = ""
            arguments = []
            for type_of_data, data in commands_metadata.items():
                if type_of_data == "description":
                    description = data
                elif type_of_data == "command":
                    command = data
                elif type_of_data == "questions":
                    for argument in data:
                        required = "required" in argument and argument["required"]
                        unique = "unique" in argument and argument["unique"]
                        rule = ""

                        if argument["name"] in VALIDATION_RULES:
                            rule = VALIDATION_RULES[argument["name"]]

                        command_arguments = {
                            "name": argument["name"],
                            "required": required,
                            "unique": unique,
                            "rule": rule,
                        }
                        arguments.append(command_arguments)
                        if argument["name"] not in all_arguments:
                            all_arguments[argument["name"]] = command_arguments

            # add a command with description
            commands_output += f"{command:<25}  - {description}"

            # add a command arguments after description
            if len(arguments) > 0:
                commands_output += f": {command}"
                for argumen in arguments:
                    name = (
                        f'<{argumen["name"]}>'
                        if argumen["required"]
                        else f'[{argumen["name"]}]'
                    )
                    commands_output += f" {name}"
            commands_output += "\n"

        internal_commands = [
            {
                "name": "help",
                "description": "used to display information about all commands: help",
            },
            {
                "name": "exit or close",
                "description": "used to close the program, data will be saved: exit",
            },
        ]

        for command in internal_commands:
            commands_output += f'{command["name"]:<25}  - {command["description"]}\n'

        print(commands_output)

        print("Types of argumets:")
        for k, v in ARGUMENT_TYPES.items():
            print(f"{k:<25} - {v}")

        if len(all_arguments) > 0:
            arguments_output = ""
            for argument in all_arguments.values():
                name = argument["name"]
                if argument["unique"]:
                    name += " (unique)"
                arguments_output += f"{name:<25}"

                if argument["rule"]:
                    arguments_output += f' - {argument["rule"]}'
                else:
                    arguments_output += " - no specific rules"
                arguments_output += "\n"

            print("\nList of arguments:")
            print(arguments_output)

    def __animate(self, data, delay=0.04):
        if not ("--silent" in sys.argv or "-s" in sys.argv):
            rows = data.split("\n")

            for row in rows:
                print(row)
                time.sleep(delay)

    def listen(self):
        commands = self.__commands

        self.__animate(logo)
        print(TEXT["WELCOME"])
        Bot.help()

        while True:
            try:
                command = request_input("Enter a command: ", commands)

                if not command:
                    continue

                cmd = parse_input(command)

                if command in EXIT_COMMANDS:
                    # if is_yes("Do you really whant to exit?"):
                    self.__animate(phrase, 0.1)
                    print(
                        "Goodbye! I hope I was useful. Thank you for using me! See you soon.\n"
                    )

                    break

                if command == self.__INTERNAL_COMMANDS["help"]:
                    Bot.help()
                    continue

                if command == self.__INTERNAL_COMMANDS["save"]:
                    self.context.address_book.save_to_file()
                    self.context.notes.save_to_file()
                    print("Saved!")
                    continue

                if cmd not in Bot.__COMMANDS_HANDLERS:
                    close_matches = difflib.get_close_matches(
                        cmd, commands, n=1, cutoff=0.6
                    )

                    if close_matches:
                        suggestion = close_matches[0]
                        print(
                            f"'{cmd}' is not a Bot command. The most similar command is '{suggestion}'"
                        )
                    else:
                        print(
                            f"'{cmd}'is not a Bot command. Use help to see commands list."
                        )

                    continue

                self.__exec(cmd)
            except ValidationValueException as err:
                print(err)
            except KeyboardInterrupt:
                print("See you later!")
                self.context.address_book.save_to_file()
                self.context.notes.save_to_file()
                break
            except Exception as err:
                print("Oops! Something went wrong!")
                print(err)

        self.context.address_book.save_to_file()
        self.context.notes.save_to_file()


__all__ = ["Bot"]
