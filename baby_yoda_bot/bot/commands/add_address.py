from baby_yoda_bot.models import Address, Context
from baby_yoda_bot.utils import print_added
from baby_yoda_bot.commands.commands import (
    CMD_ADD_ADDRESS,
    ARG_NAME,
    ARG_ADDRESS,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_ADD_ADDRESS)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_ADDRESS])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": str},
        {"name": ARG_ADDRESS, "required": True, "type": Address},
    ]
)
def add_address(ctx: Context, args):
    name, address = args
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.add_address(address)
    else:
        added = ctx.address_book.add_contact(name=str(name), address=address)
        if added:
            print_added(f'Contact "{str(name)}"')
            print_added("Address")


__all__ = ["add_address"]
