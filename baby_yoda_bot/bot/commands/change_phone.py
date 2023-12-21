from ..bot import Bot

from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("change-phone")
@Bot.description("used to change phone for a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str},
        {"name": "old_phone", "required": True, "type": str},
        {"name": "new_phone", "required": True, "type": str}
    ]
)
def change_phone(ctx: Context, args):
    name, old_phone, new_phone = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.change_phone(old_phone, new_phone)
    return f"Phone was changed from '{old_phone}'to '{new_phone}'"


__all__ = ["change_phone"]
