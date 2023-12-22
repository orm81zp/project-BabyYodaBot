from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import COMMAND_DESCRIPTION, CMD_ADD_TAG
from ..bot import Bot


@Bot.command(CMD_ADD_TAG)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_TAG])
@Bot.questions(
    [
        {"name": "Note Id", "required": True, "type": str},
        {"name": "a tag or comma separated tags", "required": True, "type": str},
    ]
)
def add_tag(ctx: Context, args):
    uuid, tags = args
    note = ctx.notes.find_one(str(uuid))

    if note:
        tags = ctx.notes.parse_tags(tags)
        note.add_tag(tags)
    else:
        print_not_found(f"Note #{uuid}")


__all__ = ["add_tag"]
