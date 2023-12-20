import pickle
from collections import UserDict
from .Record import Record
from ..utils.styled_print import StyledPrint


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
                res.append(self.data[name])
        if email != None:
            res.extend(
                list(
                    filter(
                        lambda record: record.email.value == email, self.data.values()
                    )
                )
            )
        if birthday != None:
            res.extend(
                list(
                    filter(
                        lambda record: str(record.birthday) == birthday,
                        self.data.values(),
                    )
                )
            )

        return res

    def save(self, record: Record):
        name = str(record.name)
        self.data[name] = record

    def delete(self, name: str):
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
            StyledPrint(record).print()

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
            return self.data
        except (OSError, IOError) as e:
            pass
