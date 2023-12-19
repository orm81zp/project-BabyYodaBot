import pickle
from collections import UserDict
from ..utils import generate_uuid

# TODO ADD ..utils/prin_message to AddressBook such as Deleted, Updated etc.


class AddressBook(UserDict):
    def __init__(self):
        self.filename = "AddressBookData.dat"
        super().__init__({"contacts": {}})

    def find_record(self, name, birthday, email):
        pass
        # return record

    def save_record(self, record):
        pass
        # void

    def remove_record(self, record):
        pass
        # void

    def add_record(self, record):
        pass
        # void

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
            return self.data
        except (OSError, IOError) as e:
            pass


__all__ = ["AddressBook"]
