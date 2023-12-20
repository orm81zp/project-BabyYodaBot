from .models import AddressBook

#  TODO move to logic
#  AddressBook method read_from_file and save_to_file


def start_work() -> AddressBook:
    """TODO logic to load contact book if a file exists"""
    book = AddressBook()
    return book


def save(book: AddressBook):
    """TODO logic to save contact book"""
    print("saving contact book...")


def stop_work(book: AddressBook):
    print("stoped working")
    save(book)


__all__ = [
    "start_work",
    "stop_work",
]
