import pickle
from collections import UserDict
from .note import Note
from ..utils import (
    StyledPrint,
    is_yes,
    print_not_found,
    print_added,
    print_deleted,
    print_exists,
)


class Notes(UserDict):
    uuid = 1

    def __init__(self):
        self.data = dict()
        self.filename = "NotesData.dat"

    def getId(self):
        return self.uuid

    def restoreId(self):
        if len(self.data) > 0:
            last_id = list(self.data)[-1]
            self.uuid = int(last_id)

    def generateId(self):
        self.uuid += 1
        return self.uuid

    def search(self, search_value=None):
        if search_value is None:
            return self.data
        res = list()
    
        if search_value:
             # searching by content  
            res.extend(
                list(
                    filter(
                        lambda record: str(record.content.value).lower().find(search_value.lower())  > -1,
                        self.data.values(),
                    )
                )
            )
        if search_value:
            for note in self.data.values():
               # searching by tags
                tags = note.tags
                print(tags)
                if len(tags) > 0 :
                    for tag in tags:
                        if str(tag.value).find(search_value.lower()) > -1:
                            exist = False
                            for  item in res:
                                if(item.uuid==note.uuid):
                                    exist = True
                            if not exist:
                                res.append(note)
                                continue

        if len(res) > 0:
                title = f'Search Result for "{search_value}"'
                StyledPrint(res, entity="notes").print()
        else:
                print("No results were found")


    def save(self, note: Note):
        uuid = str(note.uuid)
        data = self.find_one(uuid)
        if data:
            print_exists(f"Note {uuid}")
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
            print_not_found(f"Note {uuid}")

    def remove(self, uuid):
        if uuid in self.data:
            deleted = self.data.pop(uuid, None)
            if deleted is not None:
                print_not_found("Note")

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

    def find_note_by_tag(self, tag):
        found_notes = []
        normalized_tag = (
            tag.strip().lower()
        )  # Нормалізуємо тег до нижнього регістру та видаляємо зайві пробіли
        for title, note in self.data.items():
            normalized_tags = [
                t.strip().lower() for t in note["tags"]
            ]  # Нормалізуємо всі теги нотатки до нижнього регістру
            if normalized_tag in normalized_tags:
                found_notes.append(title)
        return found_notes

    def show_all(self):
        if len(self.data) > 0:
            StyledPrint(self.data, entity="notes").print()
        else:
            print("Nothing to display")

    def __str__(self):
        if len(self.data) == 0:
            return "Nothing to display"
        return "\n".join(str(note) for note in self.data.values())
