"""Module providing a function to change a phone number."""
from baby_yoda_bot.models import Context, Phone, Name
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_CHANGE_PHONE,
    ARG_NAME,
    ARG_OLD_PHONE,
    ARG_NEW_PHONE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_CHANGE_PHONE)
@Bot.description(COMMAND_DESCRIPTION[CMD_CHANGE_PHONE])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": Name},
        {"name": ARG_OLD_PHONE, "required": True, "type": Phone},
        {"name": ARG_NEW_PHONE, "required": True, "type": Phone},
    ]
)
def change_phone(ctx: Context, args):
    """Calls to change a phone number"""
    name, old_phone, new_phone = args
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.change_phone(str(old_phone), str(new_phone))
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["change_phone"]
