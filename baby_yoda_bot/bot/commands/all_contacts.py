"""Module providing a function to display all contacts."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import CMD_ALL_CONTACTS, COMMAND_DESCRIPTION
from ..bot import Bot


@Bot.command(CMD_ALL_CONTACTS)
@Bot.description(COMMAND_DESCRIPTION[CMD_ALL_CONTACTS])
def all_contacts(ctx: Context):
    """Calls to display all contacts"""
    ctx.address_book.show_all()


__all__ = ["all_contacts"]
