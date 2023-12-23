"""Module providing a function to remove an email."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_EMAIL,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_EMAIL)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_EMAIL])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def remove_email(ctx: Context, args):
    """Calls to remove an email"""
    name = args[0]
    contact = ctx.address_book.find_one(str(name))

    if contact:
        return contact.remove_email()
    else:
        print_not_found(f'Contact "{str(name)}"')


__all__ = ["remove_email"]
