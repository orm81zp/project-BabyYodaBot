from .common import show_help
from .commands import CMD_HELP

MAPPED_COMMANDS = {
    CMD_HELP: show_help,
}


__all__ = ["MAPPED_COMMANDS"]
