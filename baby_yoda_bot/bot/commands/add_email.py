"""Module providing a function to add an email."""
from baby_yoda_bot.models import Email, Context
from baby_yoda_bot.utils import print_added
from baby_yoda_bot.commands.commands import (
    CMD_ADD_EMAIL,
    ARG_NAME,
    ARG_EMAIL,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_ADD_EMAIL)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_EMAIL])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": str},
        {"name": ARG_EMAIL, "required": True, "type": Email},
    ]
)
def add_email(ctx: Context, args):
    """Calls to a add an email"""
    name, email = args
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.add_email(email)
    else:
        added = ctx.address_book.add_contact(name=str(name), email=email)
        if added:
            print_added(f'Contact "{str(name)}"')
            print_added("Email")


__all__ = ["add_email"]
