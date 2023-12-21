from ..bot import Bot

from baby_yoda_bot.models import Note, Context,Content


@Bot.command("add-note")
@Bot.description("used to add a note")
@Bot.questions(
    [
        {"name": "content", "required": True, "type": str},
        {"name": "tags", "required": False, "type": str}
    ]
)
def add_note(ctx: Context, args):
    content, tags = args
    id = ctx.notes.generateId()
    
    note = Note(id,silent=True)
    note.add_content(content)
    
    if tags:
        tags = tags.split(',')
        for tag in tags:
            note.add_tag(tag)

    return f"New note with id:{note.id} added."


__all__ = ["add_note"]
