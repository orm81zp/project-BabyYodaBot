from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("show-notes")
@Bot.description("used to show a contact")

def show_notes(ctx: Context, args):    
    ctx.notes.show_all()

    return ''



__all__ = ["show_notes"]
