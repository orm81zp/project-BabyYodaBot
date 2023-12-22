from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_NOTE,
    ARG_ID,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_NOTE])
@Bot.questions([{"name": ARG_ID, "required": True, "type": str}])
def remove_note(ctx: Context, args):
    id = args[0]
    ctx.notes.remove(id)


__all__ = ["remove_note"]
