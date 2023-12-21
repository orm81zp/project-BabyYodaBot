from ..bot import Bot


from baby_yoda_bot.models import Address, Context


@Bot.command("add-address")
@Bot.description("used to add birthday to the contact")
@Bot.questions(
    [
        {"name": "name", "required": True, "type": str},
        {"name": "address", "required": True, "type": Address}
    ]
)
def add_address(ctx: Context, args):
    name, address = args
    contact = ctx.address_book.find_one(name)

    if not contact:
        return f"Contact '{name}' not found"

    contact.add_address(address)
    return 'Address added'




__all__ = ["add_address"]
