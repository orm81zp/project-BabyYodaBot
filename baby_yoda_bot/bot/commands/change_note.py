"""Module providing a function to change a note."""
from baby_yoda_bot.models import Context, Content, Note, Tag
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_CHANGE_NOTE,
    COMMAND_DESCRIPTION,
    ARG_CONTENT,
    ARG_NOTE_ID,
    ARG_TAGS,
)
from ..bot import Bot


@Bot.command(CMD_CHANGE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_CHANGE_NOTE])
@Bot.questions(
    [
        {"name": ARG_NOTE_ID, "required": True, "type": str},
        {"name": ARG_CONTENT, "required": True, "type": Content},
        {"name": ARG_TAGS, "optional": True, "type": Tag, "separated_list": True},
    ]
)
def change_note(ctx: Context, args):
    """Calls to change a note"""
    uuid, content, tags = args
    uuid = str(uuid)
    note = ctx.notes.find_one(uuid)

    if note:
        note.update(content, tags)
    else:
        print_not_found(f"Note #{uuid}")


__all__ = ["change_note"]
