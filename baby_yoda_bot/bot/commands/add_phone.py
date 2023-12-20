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
@Bot.description('add phone to contact by name')
def add_phone(ctx: Context, args):
    name, phone = args

    # TODO: use find_one instad of full search
    res = ctx.address_book.find(name=name)

    if len(res) == 0:
        return f"Contact '{name}' not found"

    res[0].add_phone(phone)

    return 'Phone added'

__all__ = [
    'add_phone'
]
