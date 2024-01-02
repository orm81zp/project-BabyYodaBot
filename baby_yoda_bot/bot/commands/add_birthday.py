"""Module providing a function to add a birthday."""
from baby_yoda_bot.models import Birthday, Context, Name
from baby_yoda_bot.utils import print_added
from baby_yoda_bot.commands.commands import (
    CMD_ADD_BIRTHDAY,
    ARG_NAME,
    ARG_BIRTHDAY,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_ADD_BIRTHDAY)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_BIRTHDAY])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": Name},
        {"name": ARG_BIRTHDAY, "required": True, "type": Birthday},
    ]
)
def add_birthday(ctx: Context, args):
    """Calls to a add a birthday"""
    name, birthday = args
    name = str(name)
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.add_birthday(birthday)
    else:
        added = ctx.address_book.add_contact(name=name, birthday=birthday)
        if added:
            print_added(f'Contact "{name}"')
            print_added("Birthday")


__all__ = ["add_birthday"]
