from ..bot import Bot


from baby_yoda_bot.models import Email, Context


@Bot.command("add-email")
@Bot.description("used to add email to the contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str},
        {"name": "email", "required": True, "type": Email}
    ]
)
def add_email(ctx: Context, args):
    name, email = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.add_email(email)
    return 'Email added'




__all__ = ["add_email"]
