from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_SHOW_ADDRESS,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SHOW_ADDRESS)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_ADDRESS])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def show_address(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.show_address()
    else:
        print_not_found(f'Contact "{str(name)}"')


__all__ = ["show_address"]
