import pickle
from collections import UserDict
from .Note import Note


# TODO ADD ..utils/prin_message to AddressBook such as Deleted, Updated etc.


class Notes(UserDict):
    def __init__(self):
        self.filename = "NotesData.bob"
        super().__init__({"notes": []})

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
