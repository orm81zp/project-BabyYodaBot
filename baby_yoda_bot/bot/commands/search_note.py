from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_SEARCH_NOTE,
    ARG_SEARCH,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SEARCH_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_SEARCH_NOTE])
@Bot.questions([{"name": ARG_SEARCH, "required": True, "type": str}])
def search_note(ctx: Context, args):
    search_value = args[0]
    ctx.notes.search(search_value)


__all__ = ["search_note"]
