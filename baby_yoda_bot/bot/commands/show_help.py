"""Module providing a function to display all help information."""
from baby_yoda_bot.commands.commands import (
    VALIDATION_RULES,
    ARGUMENT_TYPES,
    COMMAND_DESCRIPTION,
    CMD_HELP,
    CMD_EXIT,
    CMD_CLOSE,
)
from ..bot import Bot


@Bot.command(CMD_HELP)
@Bot.description(COMMAND_DESCRIPTION[CMD_HELP])
def show_help(*_):
    """Calls to display help information"""
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
            "name": f"{CMD_EXIT} or {CMD_CLOSE}",
            "description": f"used to close the program, data will be saved: {CMD_EXIT}",
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


__all__ = ["show_help"]
