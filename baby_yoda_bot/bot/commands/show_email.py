from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_SHOW_EMAIL,
    ARG_NAME,
    COMMAND_DESCRIPTION,
)
from ..bot import Bot


@Bot.command(CMD_SHOW_EMAIL)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_EMAIL])
@Bot.questions([{"name": ARG_NAME, "required": True, "type": str}])
def show_email(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(str(name))

    if contact:
        contact.show_email()
    else:
        print_not_found(f'Contact "{str(name)}"')


__all__ = ["show_email"]
