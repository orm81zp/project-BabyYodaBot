from ..bot import Bot

from baby_yoda_bot.models import Note, Context


@Bot.command("add-note")
@Bot.description("used to add a note")
@Bot.questions(
    [
        {"name": "content", "required": True, "type": Context},
        {"name": "tags", "required": False, "type": str}
    ]
)
def add_note(ctx: Context, args):
    content, tags = args
    id = ctx.address_book.generateId()
    
    note = Note(id,content=content, silent=True)
    for tag in tags:
        note.add_tag(tag)

    return f"New note with id:{note.id} added."


__all__ = ["add_note"]
