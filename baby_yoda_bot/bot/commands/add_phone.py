from ..bot import Bot

from baby_yoda_bot.models import Context, Phone

@Bot.command('add-phone')
@Bot.arguments([
    {
        'name': 'name',
        'type': str
    },
    {
        'name': 'phone',
        'type': Phone
    }
])
@Bot.description('used to add a phone to a contact')
def add_phone(ctx: Context, args):
    name, phone = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.add_phone(phone)

    return 'Phone added'

__all__ = [
    'add_phone'
]
