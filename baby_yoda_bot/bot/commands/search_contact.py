from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("search-contact")
@Bot.description("used to search a contact")
@Bot.questions(
    [
        {"value": "value", "required": False, "type": str}
    ]
)
def search_contact(ctx: Context, args):
    value = args

    data = ctx.address_book.search(value)

    return data


__all__ = ["search_contact"]
