import pickle
from collections import UserDict
from .Record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(str(e))
        except KeyError as e:
            print("User not found. Please provide valid data.")
        except IndexError:
            print("Please  check your input.")

    return inner


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()
        self.filename = "AddressBookData.dat"

    # def find(self, name=None, birthday=None, email=None):
    #     if name is None and birthday is None and email is None:
    #         return self.data
    #     if name in self.data:
    #         return self.data[name]
    #     # //todo birthday search
    #     # //todo email search
    #
    #     else:
    #         print(f"User with  name  {name} not exist")

    # @input_error
    def saveRecord(self, record):
        name = str(record.name)
        self.data[name] = record

    # def find(self, name):
    #     if name in self.data:
    #         return self.data[name]
    #     else:
    #         raise KeyError(f"User with  name  {name} not exist")
    #
    # # @input_error
    # def delete(self, name):
    #     if name in self.data:
    #         del self.data[name]
    #
    # def show(self):
    #     if len(self.data) == 0:
    #         print("Address Book is empty")
    #     for record in self.data.values():
    #         print(record)
    #
    # def save_to_file(self):
    #     with open(self.filename, "wb") as file:
    #         pickle.dump(self, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
            return self.data
        except (OSError, IOError) as e:
            pass
