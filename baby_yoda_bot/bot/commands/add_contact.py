from ..bot import Bot

from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("add-contact")
@Bot.description("used to add a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": Name},
        {"name": "phone", "required": False, "type": Phone},
        {"name": "birthday", "required": False, "type": Birthday},
        {
            "name": "email",
            "required": False,
            "type": Email,
        },
    ]
)
def add_contact(ctx: Context, args):
    name, phone, birthday, email = args

    record = Record(name, silent=True)

    if birthday is not None:
        record.add_birthday(birthday)

    if email is not None:
        record.add_email(email)

    if phone is not None:
        record.add_phone(phone.value)

    ctx.address_book.save(record)

    return f"New contact with name {record.name} added."


__all__ = ["add_contact"]
