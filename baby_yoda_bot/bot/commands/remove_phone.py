from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_REMOVE_PHONE,
    ARG_NAME,
    ARG_PHONE,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_REMOVE_PHONE)
@Bot.description(COMMAND_DESCRIPTION[CMD_REMOVE_PHONE])
@Bot.questions(
    [
        {"name": ARG_NAME, "required": True, "type": str},
        {"name": ARG_PHONE, "required": True, "type": str},
    ]
)
def remove_phone(ctx: Context, args):
    name, phone = args
    contact = ctx.address_book.find_one(name)

    if contact:
        contact.remove_phone(phone)
    else:
        print_not_found(f'Contact "{str(name)}"')


__all__ = ["remove_phone"]
