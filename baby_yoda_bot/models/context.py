from baby_yoda_bot.models.address_book import address_book

class Context:
    def __init__(self):
        self.address_book = address_book()

    # TODO: implement file save/load  here
