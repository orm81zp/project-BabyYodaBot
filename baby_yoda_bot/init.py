from .models import address_book

#  TODO move to logic
#  AddressBook method read_from_file and save_to_file


def start_work() -> address_book:
    """TODO logic to load contact book if a file exists"""
    book = address_book()
    return book


def save(book: address_book):
    """TODO logic to save contact book"""
    print("saving contact book...")


def stop_work(book: address_book):
    print("stoped working")
    save(book)


__all__ = [
    "start_work",
    "stop_work",
]
