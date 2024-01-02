"""Module providing a function to display all notes."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import CMD_ALL_NOTES, COMMAND_DESCRIPTION
from ..bot import Bot


@Bot.command(CMD_ALL_NOTES)
@Bot.description(COMMAND_DESCRIPTION[CMD_ALL_NOTES])
def all_notes(ctx: Context, _):
    """Calls to display all notes"""
    ctx.notes.show_all()


__all__ = ["all_notes"]
