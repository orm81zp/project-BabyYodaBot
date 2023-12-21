from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("all-notes")
@Bot.description("used to show all notes")

def all_notes(ctx: Context, args):    
    ctx.notes.show_all()

    return ''



__all__ = ["all_notes"]
