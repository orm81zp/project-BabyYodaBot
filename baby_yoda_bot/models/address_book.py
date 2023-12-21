import pickle
from collections import UserDict
from .record import Record
from ..utils import (
    StyledPrint,
    is_yes,
    print_not_found,
    print_deleted,
    print_exists,
)


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()
        self.filename = "AddressBookData.dat"

    def find_one(self, name):
        if name in self.data:
            return self.data[name]
        return None

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

    def search(self, search_value):
        results = []
        formatted_search = search_value.lower()
        contacts = self.data.values()

        if len(contacts) > 0:
            for contact in contacts:
                potential_contact: Record = contact

                # searching by name
                if str(potential_contact.name).lower().find(formatted_search) > -1:
                    results.append(potential_contact)
                    continue
                # searching by phone number
                phones = potential_contact.phones
                if len(phones) > 0:
                    for phone in phones:
                        if str(phone).find(formatted_search) > -1:
                            results.append(potential_contact)
                            continue
                # searching by birthday
                if potential_contact.birthday:
                    if str(potential_contact.birthday).find(formatted_search) > -1:
                        results.append(potential_contact)
                        continue
                # searching by email
                if potential_contact.email:
                    if str(potential_contact.email).lower().find(formatted_search) > -1:
                        results.append(potential_contact)
                        continue
                # searching by address
                if potential_contact.address:
                    if (
                        str(potential_contact.address).lower().find(formatted_search)
                        > -1
                    ):
                        results.append(potential_contact)
                        continue

            if len(results) > 0:
                title = f'Search Result for "{search_value}"'
                StyledPrint(results, entity="contacts", title=title).print()
            else:
                print("No results were found")

        else:
            print("Address Book is empty")

    def save(self, record: Record):
        name = str(record.name)
        contact = self.find_one(name)
        if contact:
            print_exists(f"Contact {name}")

        else:
            self.data[name] = record

    def delete(self, name: str):
        if name in self.data:
            if is_yes("Existing address will be deleted, continue?"):
                is_removed = self.data.pop(name, None)
                if is_removed is not None:
                    print_deleted("Contact")
        else:
            print_not_found("Contact")

    def show(self):
        if len(self.data) == 0:
            print("Address Book is empty")
        else:
            StyledPrint(self.data, entity="contacts").print()

    def save_to_file(self):
        try:
            with open(self.filename, "wb") as file:
                pickle.dump(self.data, file)
        except (OSError, IOError):
            print("Oh! Something went wrong while saving the contact book!")

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
                print(f"Contact book {self.filename} restored!")
        except (OSError, IOError):
            print("Oh! Something went wrong while restoring the contact book!")

    def __str__(self):
        if len(self.data) > 0:
            return "\n".join([str(record) for record in self.data.values()])
        return "Address Book is empty"
