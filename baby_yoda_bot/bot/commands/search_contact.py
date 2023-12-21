from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_SEARCH_CONTACT,
    ARG_SEARCH,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SEARCH_CONTACT)
@Bot.description(COMMAND_DESCRIPTION[CMD_SEARCH_CONTACT])
@Bot.questions([{"name": ARG_SEARCH, "required": True, "type": str}])
def search_contact(ctx: Context, args):
    search_value = args[0]
    ctx.address_book.search(search_value)


__all__ = ["search_contact"]
