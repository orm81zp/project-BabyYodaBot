import time
import sys
import inspect
import difflib
from collections import defaultdict

from ..assets import logo, phrase
from baby_yoda_bot.models.context import Context
from baby_yoda_bot.utils import request_input, parse_input
from baby_yoda_bot.exceptions.exceptions import ValidationValueException


class Bot:
    __COMMANDS_HANDLERS = {}
    __COMMANDS_METADATA__ = defaultdict(dict)

    __EXIT_COMMANDS = ["exit", "close"]
    __INTERNAL_COMMANDS = {
        "help": "help",
        "save": "save",
    }

    @property
    def __commands(self):
        commands = list(Bot.__COMMANDS_HANDLERS.keys())
        commands.extend(self.__INTERNAL_COMMANDS.values())
        commands.extend(self.__EXIT_COMMANDS)

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
    def arguments(args):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__[key]["arguments"] = args

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

    def __exec(self, command, args):
        executor_args = [self.context]
        executor = Bot.__COMMANDS_HANDLERS[command]

        metadata_key = executor.__bot_cmd__
        metadata = Bot.__COMMANDS_METADATA__[metadata_key]

        if "questions" in metadata:
            validated_args = []

            for rule in metadata["questions"]:
                is_optional = not rule["required"] if "required" in rule else False

                while True:
                    optional = "(optional)" if is_optional else ""
                    value = input(f"Enter {rule['name']}{optional}: ")

                    if not value and is_optional:
                        value = None
                        break

                    if "type" in rule:
                        try:
                            value = rule["type"](value)
                            break
                        except ValidationValueException as e:
                            print(e)
                            continue

                validated_args.append(value)
            executor_args.append(validated_args)

        if "arguments" in metadata:
            if len(metadata["arguments"]) != len(args):
                expected_args = ", ".join(
                    [f"<{arg['name']}>" for arg in metadata["arguments"]]
                )

                return f"Invalid number of arguments, expected: {expected_args}"

            validated_args = []

            for i, rule in enumerate(metadata["arguments"]):
                name = rule["name"]
                validation_type = rule["type"]
                value = args[i]

                try:
                    validated_args.append(type(validation_type))
                except ValidationValueException as e:
                    return f"Argument {name}='{value}' is invalid: {e}"

            executor_args.append(validated_args)

        required_args = inspect.getfullargspec(executor).args

        if len(required_args) == 2 and len(executor_args) == 1:
            executor_args.append([])

        return executor(*executor_args)

    def help(self):
        print("Commands list:")

        for metadata in Bot.__COMMANDS_METADATA__.values():
            arguments_list = ""
            command = metadata["command"]
            description = metadata["description"] if "description" in metadata else ""

            arguments = metadata["arguments"] if "arguments" in metadata else []

            if len(arguments):
                arguments_list = ", ".join([f"<{arg['name']}>" for arg in arguments])

            print(f"{command} {arguments_list} - {description}")

    def __animate(self, data, delay=0.04):
        if not ("--silent" in sys.argv or "-s" in sys.argv):
            rows = data.split("\n")

            for row in rows:
                print(row)
                time.sleep(delay)

    def listen(self):
        commands = self.__commands

        self.__animate(logo)

        while True:
            try:
                command = request_input("Enter command: ", commands)

                if not command:
                    continue

                cmd, args = parse_input(command)

                if command in Bot.__EXIT_COMMANDS:
                    self.__animate(phrase, 0.1)
                    print(
                        "Goodbye! I hope I was useful. Thank you for using me.! See you soon.\n"
                    )

                    break

                if command == self.__INTERNAL_COMMANDS["help"]:
                    self.help()
                    continue

                if command == self.__INTERNAL_COMMANDS["save"]:
                    self.context.address_book.save_to_file()
                    print("Saved!")
                    continue

                if cmd not in Bot.__COMMANDS_HANDLERS:
                    close_matches = difflib.get_close_matches(
                        cmd, commands, n=1, cutoff=0.6
                    )

                    if close_matches:
                        suggestion = close_matches[0]
                        print(f"Unknown command '{cmd}'. Do you mean '{suggestion}'?")
                    else:
                        print(f"Unknown command '{cmd}', use help to see commands list")

                    continue

                output = self.__exec(cmd, args)
                print(output)
            except KeyboardInterrupt:
                print("See you later!")
                self.context.address_book.save_to_file()
                self.context.notes.save_to_file()
                break
            except Exception as e:
                print("Oops! Something went wrong!")
                print(e)
                break

        self.context.address_book.save_to_file()


__all__ = ["Bot"]
