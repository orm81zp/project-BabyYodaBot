"""Module providing a function to change a phone number."""
from baby_yoda_bot.models import Context
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
        {"name": ARG_NAME, "required": True, "type": str},
        {"name": ARG_OLD_PHONE, "required": True, "type": str},
        {"name": ARG_NEW_PHONE, "required": True, "type": str},
    ]
)
def change_phone(ctx: Context, args):
    """Calls to change a phone number"""
    name, old_phone, new_phone = args
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.change_phone(old_phone, new_phone)
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["change_phone"]
