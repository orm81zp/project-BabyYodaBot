"""Module providing a function to remove an address."""
from baby_yoda_bot.models import Context, Name
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_ADDRESS,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_ADDRESS)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_ADDRESS])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": Name}])
def remove_address(ctx: Context, args):
    """Calls to remove an address"""
    name = args[0]
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.remove_address()

    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["remove_address"]
