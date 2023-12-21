from ..bot import Bot

from baby_yoda_bot.models import Context


@Bot.command("remove-phone")
@Bot.description("used to remove phone for a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str},
        {"name": "phone", "required": True, "type": str},

    ]
)
def remove_phone(ctx: Context, args):
    name, phone = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.remove_phone(phone)
    return f"Phone '{phone}' was removed"


__all__ = ["remove_phone"]
