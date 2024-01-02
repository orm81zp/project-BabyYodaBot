"""Module providing a function to  show birthdays."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_BIRTHDAYS,
    COMMAND_DESCRIPTION,
    ARG_BIRTHDAY_RANGE,
    VALIDATION_RULES,
)
from ..bot import Bot


@Bot.command(CMD_BIRTHDAYS)
@Bot.description(COMMAND_DESCRIPTION[CMD_BIRTHDAYS])
@Bot.questions(
    [
        {
            "name": ARG_BIRTHDAY_RANGE,
            "required": False,
            "type": str,
            "pattern": r"^(\d+|\d{2}\.\d{2})$",
            "pattern_error": VALIDATION_RULES[ARG_BIRTHDAY_RANGE],
        }
    ]
)
def birthdays(ctx: Context, args):
    """Calls to display birthdays"""
    birthday_range = args[0]
    ctx.address_book.birthdays(birthday_range)


__all__ = ["birthdays"]
