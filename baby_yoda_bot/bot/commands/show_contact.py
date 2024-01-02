"""Module providing a function to display a contact."""
from baby_yoda_bot.models import Context, Name
from baby_yoda_bot.commands.commands import (
    CMD_SHOW_CONTACT,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SHOW_CONTACT)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_CONTACT])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": Name}])
def show_contact(ctx: Context, args):
    """Calls to display a contact"""
    name = args[0]
    ctx.address_book.show_contact(str(name))


__all__ = ["show_contact"]
