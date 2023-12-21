from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("show-note")
@Bot.description("used to show a contact")
@Bot.questions(
    [
        {"name": "id", "required": True, "type": str}
    ]
)
def show_note(ctx: Context, args):
    id = args[0]
    notes = ctx.notes.find_one(id)

    if not notes:
        return f"Notee '{id}' not found"

    data = ctx.notes.show_note(id)

    return data


__all__ = ["show_note"]
