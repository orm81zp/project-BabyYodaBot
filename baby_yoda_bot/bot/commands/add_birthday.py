from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("add-birthday")
@Bot.description("used to remove a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str},
        {"name": "birthday", "required": True, "type": Birthday}
    ]
)
def add_birthday(ctx: Context, args):
    name, birthday = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.add_birthday(birthday)
    return 'Birthday added'




__all__ = ["add_birthday"]
