from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("search-contact")
@Bot.description("used to search a contact")
@Bot.questions(
    [
        {"search": "search", "required": False, "type": str}
    ]
)
def search_contact(ctx: Context, args):
    search = args

    data = ctx.address_book.search(search)

    return data


__all__ = ["search_contact"]
