from baby_yoda_bot.models.address_book import AddressBook

class Context:
    def __init__(self):
        self.address_book = AddressBook()
        self.address_book.read_from_file()
        # self.notes.read_from_file()
    # TODO: implement file save/load  here
