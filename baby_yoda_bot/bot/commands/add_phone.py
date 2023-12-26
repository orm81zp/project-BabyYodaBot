"""Module providing a function to add a phone number."""
from baby_yoda_bot.models import Context, Phone
from baby_yoda_bot.utils import print_added
from baby_yoda_bot.commands.commands import (
    CMD_ADD_PHONE,
    ARG_NAME,
    ARG_PHONE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_ADD_PHONE)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_PHONE])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": str},
        {"name": ARG_PHONE, "required": True, "type": Phone},
    ]
)
def add_phone(ctx: Context, args):
    """Calls to a add a phone number"""
    name, phone = args
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.add_phone(str(phone))
    else:
        added = ctx.address_book.add_contact(name=str(name), phone=phone)
        if added:
            print_added(f'Contact "{str(name)}"')
            print_added("Phone number")


__all__ = ["add_phone"]
