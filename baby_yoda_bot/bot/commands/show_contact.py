from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_SHOW_CONTACT,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SHOW_CONTACT)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_CONTACT])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def show_contact(ctx: Context, args):
    name = str(args[0])
    ctx.address_book.show_contact(name)


__all__ = ["show_contact"]
