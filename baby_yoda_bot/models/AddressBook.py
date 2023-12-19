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

    def find(self, name=None, birthday=None, email=None):
        if name is None and birthday is None and email is None:
            return self.data
        res = list()
        if name != None:
            if name in self.data:
                return res.append(self.data[name])
        if email != None:
            return filter(lambda record: record.email.value == email, self.data)

        # //todo birthday search
        # //todo email search

        else:
            print(f"User with  name  {name} not exist")

    # @input_error
    def save(self, record):
        name = str(record.name)
        self.data[name] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if len(self.data) == 0:
            print("Address Book is empty")
        for record in self.data.values():
            print(record)

    def show(self):
        if len(self.data) == 0:
            print("Address Book is empty")
        for record in self.data.values():
            print(record)

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
