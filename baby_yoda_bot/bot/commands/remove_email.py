from ..bot import Bot


from baby_yoda_bot.models import Context


@Bot.command("remove-email")
@Bot.description("used to remove email from the contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def remove_email(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"


    return contact.remove_email()


__all__ = ["remove_email"]
