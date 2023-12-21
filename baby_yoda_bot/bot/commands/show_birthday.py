from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("show-birthday")
@Bot.description("used to show a birthday for a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def show_birthday(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"


    return contact.show_birthday()


__all__ = ["show_birthday"]
