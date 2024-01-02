"""Module providing a function to save contacts and notes."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import COMMAND_DESCRIPTION, CMD_SAVE
from ..bot import Bot


@Bot.command(CMD_SAVE)
@Bot.description(COMMAND_DESCRIPTION[CMD_SAVE])
def save(ctx: Context):
    """Calls to save contacts and notes"""
    ctx.address_book.save_to_file()
    ctx.notes.save_to_file()
    print("Saved!")


__all__ = ["save"]
