"""Module providing a function to add a note."""
from baby_yoda_bot.models import Note, Context, Content
from baby_yoda_bot.commands.commands import (
    CMD_ADD_NOTE,
    COMMAND_DESCRIPTION,
    ARG_CONTENT,
)
from ..bot import Bot


@Bot.command(CMD_ADD_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_NOTE])
@Bot.questions(
    [
        {"name": ARG_CONTENT, "required": True, "type": Content},
        {
            "name": "a tag or comma separated tags",
            "required": False,
            "type": str,
        },
    ]
)
def add_note(ctx: Context, args):
    """Calls to a add a note"""
    content, tags = args
    tags = ctx.notes.parse_tags(tags)
    uuid = ctx.notes.generateId()
    note = Note(uuid, content=content, tags=tags)
    ctx.notes.save(note)


__all__ = ["add_note"]
