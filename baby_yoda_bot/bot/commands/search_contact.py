from ..bot import Bot


from baby_yoda_bot.models import Name, Phone, Birthday, Email, Record, Context


@Bot.command("search-contact")
@Bot.description("used to search a contact")
@Bot.questions(
    [
        {"name": "search", "required": False, "type": str}
    ]
)
def search_contact(ctx: Context, args):
    data = ctx.address_book.search(args[0])

    return data


__all__ = ["search_contact"]
