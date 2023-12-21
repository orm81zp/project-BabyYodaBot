from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_ADDRESS,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_ADDRESS)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_ADDRESS])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def remove_address(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.remove_address()

    else:
        print_not_found(f'Contact "{str(name)}"')


__all__ = ["remove_address"]
