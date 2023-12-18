from .mapper import MAPPED_COMMANDS


def commands_handler(command, book, args):
    if command in MAPPED_COMMANDS:
        MAPPED_COMMANDS[command](book, args)


__all__ = ["commands_handler"]
