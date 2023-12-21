from ..bot import Bot

from baby_yoda_bot.models import name, phone, birthday, email, record, Context

@Bot.command('add-contact')
@Bot.description('used to add a contact')
@Bot.questions([
    {
        'name': 'name',
        'required': True,
        'type': name
    },
    {
        'name': 'phone',
        'required': False,
        'type': phone
    },
    {
        'name': 'birthday',
        'required': False,
        'type': birthday
    },
    {
        'name': 'email',
        'required': False,
        'type': email,
    }
])
def add_contact(ctx: Context, args):
    name, phone, birthday, email = args

    record = record(name)

    if birthday is not None:
        record.add_birthday(birthday)
    
    if email is not None:
        record.add_address(email)

    if phone is not None:
        record.add_phone(phone.value)

    ctx.address_book.save(record)

    return f'New contact added {str(record)}'

__all__ = [
    'add_contact'
]
