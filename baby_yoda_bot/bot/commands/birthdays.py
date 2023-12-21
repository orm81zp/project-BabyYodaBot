from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("birthdays")
@Bot.description("used to show a contact")
@Bot.questions(
    [
        {"name": "date", "required": True, "type": str}
    ]
)
def birthdays(ctx: Context, args):
    date = args[0]
    contacts = ctx.address_book.find(birthday=date)
    # TODO it doesn't work as expected
    return contacts


__all__ = ["birthdays"]