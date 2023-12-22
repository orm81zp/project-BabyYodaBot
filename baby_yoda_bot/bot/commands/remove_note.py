from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_NOTE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_NOTE])
@Bot.questions([{"name": "Note Id", "required": True, "type": str}])
def remove_note(ctx: Context, args):
    uuid = args[0]
    ctx.notes.remove(str(uuid))


__all__ = ["remove_note"]
