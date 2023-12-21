from ..bot import Bot


from baby_yoda_bot.models import Context


@Bot.command("show-phones")
@Bot.description("used to show phones from the contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def show_phones(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    return  contact.show_phones()


__all__ = ["show_phones"]
