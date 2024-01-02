"""Module providing a function to remove a note."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_NOTE,
    COMMAND_DESCRIPTION,
    ARG_NOTE_ID,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_NOTE])
@Bot.questions([{"name": ARG_NOTE_ID, "required": True, "type": str}])
def remove_note(ctx: Context, args):
    """Calls to remove a note"""
    uuid = args[0]
    ctx.notes.remove(str(uuid))


__all__ = ["remove_note"]
