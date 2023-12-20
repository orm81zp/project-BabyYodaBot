from .BaseCommand import BaseCommand


class ShowContact(BaseCommand):
    def __init__(self):
        super().__init__()
        self.address_book.show()
