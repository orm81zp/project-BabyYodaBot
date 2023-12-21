from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("search-contact")
@Bot.description("used to search a contact by name")
@Bot.questions(
    [
        {"name": "search", "required": True, "type": str}
    ]
)
def search_contact(ctx: Context, args):
    data = ctx.address_book.search(args[0])

    return data


__all__ = ["search_contact"]
