from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import COMMAND_DESCRIPTION, CMD_ALL_TAGS
from ..bot import Bot


@Bot.command(CMD_ALL_TAGS)
@Bot.description(COMMAND_DESCRIPTION[CMD_ALL_TAGS])
def all_tags(ctx: Context, _):
    ctx.notes.show_all_tags()


__all__ = ["all_tags"]
