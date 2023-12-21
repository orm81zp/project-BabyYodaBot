from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import (
    CMD_BIRTHDAYS,
    COMMAND_DESCRIPTION,
    ARG_BIRTHDAY_RANGE,
)
from ..bot import Bot
from ...utils import StyledPrint


@Bot.command(CMD_BIRTHDAYS)
@Bot.description(COMMAND_DESCRIPTION[CMD_BIRTHDAYS])
@Bot.questions([{"name": ARG_BIRTHDAY_RANGE, "required": True, "type": str}])
def birthdays(ctx: Context, args):
    date = args[0]
    contacts = ctx.address_book.find(birthday=date)
    # TODO  it doesn't work as expected
    for contact in contacts:
        StyledPrint(contact, entity="contact").print()


__all__ = ["birthdays"]
