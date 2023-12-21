from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("remove-contact")
@Bot.description("used to remove a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def remove_contact(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)
    if not contact:
        return f"Contact '{name}' not found"
    ctx.address_book.remove(name)



__all__ = ["remove_contact"]
