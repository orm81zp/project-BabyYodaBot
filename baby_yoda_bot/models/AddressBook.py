from collections import UserDict
from ..utils import generate_uuid

# TODO ADD ..utils/prin_message to AddressBook such as Deleted, Updated etc.


class AddressBook(UserDict):
    def __init__(self):
        super().__init__({"contacts": {}, "notes": []})

    def find(self, name):
        for contact in self.data["contacts"].values():
            if contact.name.value == name:
                return contact
        return None

    def find_with_key(self, name):
        for key, contact in self.data["contacts"].items():
            if contact.name.value == name:
                return (key, contact)
        return (None, None)

    def find_note(self, index):
        for note in self.data["notes"]:
            if note.uuid == index:
                return note
        return None

    def find_note_by_content(self, content):
        for note in self.data["notes"]:
            if note.value == content:
                return note
        return None

    def add_record(self, contact):
        uuid = generate_uuid()
        self.data["contacts"][uuid] = contact

    # contact methods
    def add_contact(self):
        pass

    def show_contact(self):
        pass

    def change_contact(self):
        pass

    def remove_contact(self):
        pass

    def all_contact(self):
        pass

    # birthday methods
    def add_birthday(self):
        pass

    def show_birthday(self):
        pass

    def remove_birthday(self):
        pass

    # email methods
    def add_email(self):
        pass

    def show_email(self):
        pass

    def remove_email(self):
        pass

    # address methods
    def add_address(self):
        pass

    def show_address(self):
        pass

    def remove_address(self):
        pass

    # phone methods
    def add_phone(self):
        pass

    def show_phone(self):
        pass

    def change_phone(self):
        pass

    def remove_phone(self):
        pass

    # note methods
    def add_note(self):
        pass

    def show_note(self):
        pass

    def remove_note(self):
        pass


__all__ = ["AddressBook"]
