from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("remove-birthday")
@Bot.description("used to remove birthday for a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def remove_birthday(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)
    if not contact:
        return f"Contact '{name}' not found"
    contact.remove_birthday()



__all__ = ["remove_birthday"]
