from ..bot import Bot


from baby_yoda_bot.models import  Context


@Bot.command("show-address")
@Bot.description("used to show a address for a contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str}
    ]
)
def show_address(ctx: Context, args):
    name = args[0]
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"


    return contact.show_address()


__all__ = ["show_address"]
