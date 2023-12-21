from baby_yoda_bot.models.address_book import AddressBook
from baby_yoda_bot.models.notes import Notes
class Context:
    def __init__(self):
        self.address_book = AddressBook()
        self.address_book.read_from_file()
        self.notes = Notes()
        self.notes.read_from_file()

