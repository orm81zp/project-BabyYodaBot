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
    ARG_ID = args[0]
    print(ARG_ID)
    ctx.notes.remove(ARG_ID)


__all__ = ["remove_note"]
