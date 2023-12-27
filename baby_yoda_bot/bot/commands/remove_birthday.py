"""Module providing a function to remove a birthday."""
from baby_yoda_bot.models import Context, Name
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_BIRTHDAY,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_BIRTHDAY)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_BIRTHDAY])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": Name}])
def remove_birthday(ctx: Context, args):
    """Calls to remove a birthday"""
    name = args[0]
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.remove_birthday()
    else:
        print_not_found(f'Contact "{name}"')


__all__ = ["remove_birthday"]
