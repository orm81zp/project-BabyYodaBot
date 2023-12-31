from baby_yoda_bot.models import Context
from baby_yoda_bot.commands.commands import CMD_SHOW_NOTE, COMMAND_DESCRIPTION
from ..bot import Bot


@Bot.command(CMD_SHOW_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_SHOW_NOTE])
@Bot.questions([{"name": "Note Id", "required": True, "type": str}])
def show_note(ctx: Context, args):
    uuid = args[0]
    ctx.notes.show_note(uuid)


__all__ = ["show_note"]
