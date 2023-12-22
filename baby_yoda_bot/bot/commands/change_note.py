from baby_yoda_bot.models import Context, Content, Note
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_CHANGE_NOTE,
    COMMAND_DESCRIPTION,
    ARG_CONTENT,
)
from ..bot import Bot


@Bot.command(CMD_CHANGE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_CHANGE_NOTE])
@Bot.questions(
    [
        {"name": "Note Id", "required": True, "type": str},
        {"name": ARG_CONTENT, "required": True, "type": Content},
        {"name": "a tag or comma separated tags", "optional": True, "type": str},
    ]
)
def change_note(ctx: Context, args):
    uuid, content, tags = args
    note = ctx.notes.find_one(str(uuid))

    if note:
        tags = ctx.notes.parse_tags(tags)
        updated_note = Note(uuid, content=content, tags=tags)
        ctx.notes.save(updated_note)
    else:
        print_not_found(f"Note #{uuid}")


__all__ = ["change_note"]
