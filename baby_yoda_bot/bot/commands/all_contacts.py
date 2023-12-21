from ..bot import Bot

from baby_yoda_bot.models import  Context

@Bot.command('all-contacts')
@Bot.description('shows all the contacts')
def all_contacts(ctx: Context):    
    ctx.address_book.show_all()

    return ''

__all__ = [
    'all_contacts'
]
