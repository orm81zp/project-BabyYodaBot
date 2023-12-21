from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("show-email")
@Bot.description("used to show a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def show_email(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"



    return contact.show_email()


__all__ = ["show_email"]
