"""Module providing a function to search and display notes found by a tag."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_SEARCH_BY_TAG,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SEARCH_BY_TAG)
@Bot.description(COMMAND_DESCRIPTION[CMD_SEARCH_BY_TAG])
@Bot.questions(
    [
        {"name": "a tag", "required": True, "type": str},
    ]
)
def search_by_tag(ctx: Context, args):
    """Calls to search and display notes found by a tag"""
    tag = args[0]
    ctx.notes.search_by_tag(tag.strip())


__all__ = ["search_by_tag"]
