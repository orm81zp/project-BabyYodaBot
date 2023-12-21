from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_CONTACT,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_CONTACT)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_CONTACT])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def remove_contact(ctx: Context, args):
    name = args[0]
    ctx.address_book.remove(str(name))


__all__ = ["remove_contact"]
