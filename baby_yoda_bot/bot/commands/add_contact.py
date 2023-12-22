from baby_yoda_bot.models import Name, Phone, Birthday, Email, Context
from baby_yoda_bot.utils import print_added
from baby_yoda_bot.commands.commands import (
    CMD_ADD_CONTACT,
    ARG_NAME,
    ARG_BIRTHDAY,
    ARG_PHONE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_ADD_CONTACT)
@Bot.description(COMMAND_DESCRIPTION[CMD_ADD_CONTACT])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": Name, "unique": True},
        {"name": ARG_PHONE, "required": False, "type": Phone},
        {"name": ARG_BIRTHDAY, "required": False, "type": Birthday},
        {
            "name": "email",
            "required": False,
            "type": Email,
        },
    ]
)
def add_contact(ctx: Context, args):
    name, phone, birthday, email = args
    added = ctx.address_book.add_contact(
        name, phone=phone, birthday=birthday, email=email
    )

    if added:
        print_added(f'Contact "{str(name)}"')


__all__ = ["add_contact"]
