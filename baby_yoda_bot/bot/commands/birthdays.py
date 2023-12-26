"""Module providing a function to show birthdays."""
from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import CMD_BIRTHDAYS, COMMAND_DESCRIPTION
from ..bot import Bot


@Bot.command(CMD_BIRTHDAYS)
@Bot.description(COMMAND_DESCRIPTION[CMD_BIRTHDAYS])
@Bot.questions(
    [
        {
            "name": "days range (7 by default) or a date (DD.MM)",
            "required": True,
            "type": str,
        }
    ]
)
def birthdays(ctx: Context, args):
    """Calls to display birthdays."""
    birthday_range = args[0]
    ctx.address_book.birthdays(birthday_range)


__all__ = ["birthdays"]
