from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("show-contact")
@Bot.description("used to show a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def show_contact(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    data = ctx.address_book.show_contact(name)

    return data


__all__ = ["show_contact"]
