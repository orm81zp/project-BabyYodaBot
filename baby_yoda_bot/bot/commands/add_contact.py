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
    ctx.address_book.add_contact(args)


__all__ = ["add_contact"]
