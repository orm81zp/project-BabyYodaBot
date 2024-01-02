"""Module providing a function to search and display notes found by a tag."""
from baby_yoda_bot.models import Context, Tag
from baby_yoda_bot.commands.commands import (
    CMD_SEARCH_BY_TAG,
    COMMAND_DESCRIPTION,
    ARG_TAG,
)
from ..bot import Bot


@Bot.command(CMD_SEARCH_BY_TAG)
@Bot.description(COMMAND_DESCRIPTION[CMD_SEARCH_BY_TAG])
@Bot.questions(
    [
        {"name": ARG_TAG, "required": True, "type": Tag},
    ]
)
def search_by_tag(ctx: Context, args):
    """Calls to search and display notes found by a tag"""
    tag = args[0]
    ctx.notes.search_by_tag(str(tag))


__all__ = ["search_by_tag"]
