from ..bot import Bot

from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context

@Bot.command('add-contact')
@Bot.description('used to add a contact')
@Bot.questions([
    {
        'name': 'name',
        'required': True,
        'type': Name
    },
    {
        'name': 'phone',
        'required': False,
        'type': Phone
    },
    {
        'name': 'birthday',
        'required': False,
        'type': Birthday
    },
    {
        'name': 'email',
        'required': False,
        'type': Email,
    }
])
def add_contact(ctx: Context, args):
    name, phone, birthday, email = args

    record = Record(name)
    record.add_birthday(birthday)
    record.add_address(email)

    if phone is not None:
        record.add_phone(phone)

    ctx.address_book.save(record)

    return f'New contact added {str(record)}'

__all__ = [
    'add_contact'
]
