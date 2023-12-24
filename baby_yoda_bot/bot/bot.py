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
    ARG_NAME,
    ARG_OLD_PHONE,
)
from ..assets import logo, phrase


class Bot:
    __COMMANDS_HANDLERS = {}
    __COMMANDS_METADATA__ = defaultdict(dict)

    __WIZARD_CLOSE_COMMAND = "-exit"

    @property
    def __commands(self):
        commands = list(Bot.__COMMANDS_HANDLERS.keys())
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
                f":mage: I'm collecting your data...\nSay {self.__WIZARD_CLOSE_COMMAND} to stop!"
            )
            history = {}
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
                    elif rule["name"] == ARG_OLD_PHONE and "name" in history:
                        contact = self.context.address_book.find_one(history["name"])
                        if contact:
                            compeltions = contact.get_list_of_phones()

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

                    if rule["name"] == ARG_NAME:
                        history["name"] = value

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

                validated_args.append(value)
            executor_args.append(validated_args)

        required_args = inspect.getfullargspec(executor).args

        if len(required_args) == 2 and len(executor_args) == 1:
            executor_args.append([])

        return executor(*executor_args)

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
        self.__exec("help")

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
