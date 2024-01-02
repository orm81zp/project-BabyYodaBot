"""Module providing a function to remove a tag or tags."""
from baby_yoda_bot.models import Context, Tag
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    COMMAND_DESCRIPTION,
    CMD_REMOVE_TAG,
    ARG_NOTE_ID,
    ARG_TAGS,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_TAG)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_TAG])
@Bot.questions(
    [
        {"name": ARG_NOTE_ID, "required": True, "type": str},
        {"name": ARG_TAGS, "required": True, "type": Tag, "separated_list": True},
    ]
)
def remove_tag(ctx: Context, args):
    """Calls to remove a tag"""
    uuid, tags = args
    uuid = str(uuid)
    note = ctx.notes.find_one(uuid)

    if note:
        note.remove_tag(tags)
    else:
        print_not_found(f"Note #{uuid}")


__all__ = ["remove_tag"]
