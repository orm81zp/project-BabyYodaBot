"""Module providing a function to remove an email."""
from baby_yoda_bot.models import Context, Name
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_EMAIL,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_EMAIL)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_EMAIL])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": Name}])
def remove_email(ctx: Context, args):
    """Calls to remove an email"""
    name = args[0]
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        return contact.remove_email()
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["remove_email"]
