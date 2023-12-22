import pickle
from collections import UserDict
from ..utils import (
    StyledPrint,
    print_not_found,
    print_added,
    print_updated,
    print_deleted,
)
from .note import Note


class Notes(UserDict):
    uuid = 1

    def __init__(self):
        self.data = dict()
        self.filename = "yoda_bot_notes.dat"

    def getId(self):
        return self.uuid

    def restoreId(self):
        if len(self.data) > 0:
            last_id = list(self.data)[-1]
            self.uuid = int(last_id)

    def generateId(self):
        self.uuid += 1
        return self.uuid

    def parse_tags(self, tags):
        if tags:
            tags = tags.split(",") if "," in tags else tags.split(" ")
            tags = list(map((lambda x: x.strip()), tags))
            return tags
        return []

    def search(self, search_value=None):
        notes = []

        if search_value:
            search_formatted = search_value.lower()
            for note in self.data.values():
                # searching by content
                if str(note.content).lower().find(search_formatted) > -1:
                    notes.append(note)
                    continue

                # searching by tags if by content not found
                for tag in note.tags:
                    if str(tag).find(search_formatted) > -1:
                        notes.append(note)
                        break

            if len(notes) > 0:
                title = f'Search Result for "{search_value}"'
                StyledPrint(notes, entity="notes", title=title).print()
            else:
                print("Nothing to display.")
        else:
            print("No search query specified.")

    def save(self, note: Note):
        uuid = str(note.uuid)
        existed_note = self.find_one(uuid)
        if existed_note:
            self.data[uuid] = note
            print_updated(f"Note #{uuid}")
        else:
            self.data[uuid] = note
            print_added("Note")

    def find_one(self, uuid):
        if uuid in self.data:
            return self.data[uuid]
        return None

    def show_note(self, uuid):
        note = self.find_one(uuid)
        if note:
            StyledPrint(note, entity="note").print()
        else:
            print_not_found(f"Note #{uuid}")

    def remove(self, uuid):
        if uuid in self.data:
            deleted = self.data.pop(uuid, None)
            if deleted is not None:
                print_deleted(f"Note #{uuid}")

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
                self.restoreId()
            return self.data
        except (OSError, IOError) as e:
            pass

    def search_by_tag(self, tag):
        notes = []
        for note in self.data.values():
            tags = [str(t).lower() for t in note.tags]
            if tag.lower() in tags:
                notes.append(note)

        if len(notes) > 0:
            title = f"Search Result by #{tag} tag"
            StyledPrint(notes, entity="notes", title=title).print()
        else:
            print("Nothing to display.")

    def show_all(self):
        if len(self.data) > 0:
            StyledPrint(self.data, entity="notes").print()
        else:
            print("Nothing to display.")

    def show_all_tags(self):
        if len(self.data) > 0:
            tags = set()
            for note in self.data.values():
                for tag in note.tags:
                    tags.add(str(tag))

            if len(tags) > 0:
                print(f"({len(tags)}) " + (", ".join(tags)))
            else:
                print("Nothing to display.")

        else:
            print_not_found("Notes")

    def __str__(self):
        if len(self.data) == 0:
            return "Nothing to display."
        return "\n".join(str(note) for note in self.data.values())
