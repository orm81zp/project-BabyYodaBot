"""Module providing a function to display a phone or phones numbers."""
from baby_yoda_bot.models import Context, Name
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_SHOW_PHONE,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SHOW_PHONE)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_PHONE])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": Name}])
def show_phone(ctx: Context, args):
    """Calls to display a phone or phones numbers"""
    name = args[0]
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.show_phone()
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["show_phone"]
