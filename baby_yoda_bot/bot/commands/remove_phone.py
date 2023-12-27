"""Module providing a function to remove a phone number."""
from baby_yoda_bot.models import Context, Name, Phone
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_PHONE,
    ARG_NAME,
    ARG_PHONE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_PHONE)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_PHONE])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": Name},
        {"name": ARG_PHONE, "required": True, "type": Phone},
    ]
)
def remove_phone(ctx: Context, args):
    """Calls to remove a phone"""
    name, phone = args
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.remove_phone(str(phone))
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["remove_phone"]
