from baby_yoda_bot.models import Note, Context, Content
from baby_yoda_bot.commands.commands import CMD_ADD_NOTE, COMMAND_DESCRIPTION
from ..bot import Bot


@Bot.command(CMD_ADD_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_NOTE])
@Bot.questions(
    [
        {"name": "content", "required": True, "type": Content},
        {
            "name": "tags, separated only by commas or spaces",
            "required": False,
            "type": str,
        },
    ]
)
def add_note(ctx: Context, args):
    content, tags = args

    if tags:
        tags = tags.split(",") if "," in tags else tags.split(" ")
        tags = list(map((lambda x: x.strip()), tags))

    uuid = ctx.notes.generateId()
    note = Note(uuid, content=content, tags=tags)
    ctx.notes.save(note)


__all__ = ["add_note"]
