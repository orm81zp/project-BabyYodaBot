from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_BIRTHDAYS,
    COMMAND_DESCRIPTION,
    ARG_BIRTHDAY_RANGE,
)
from ..bot import Bot


@Bot.command(CMD_BIRTHDAYS)
@Bot.description(COMMAND_DESCRIPTION[CMD_BIRTHDAYS])
@Bot.questions(
    [
        {
            "name": ARG_BIRTHDAY_RANGE,
            "required": True,
            "type": str,
        }
    ]
)
def birthdays(ctx: Context, args):
    birthday_range = args[0]
    ctx.address_book.birthdays(birthday_range)


__all__ = ["birthdays"]
