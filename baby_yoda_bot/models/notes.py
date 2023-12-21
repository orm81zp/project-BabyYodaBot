import pickle
from collections import UserDict
from .note import Note


class Notes(UserDict):
    def __init__(self):
        self.data = dict()
        self.filename = "NotesData.dat"

    def find(self, title=None, content=None, tags=None):
        if title is None and content is None and tags is None:
            return self.data
        res = list()
        if title != None:
            if title in self.data:
                res.append(self.data[title])
        if content != None:
            res.extend(
                list(
                    filter(
                        lambda record: record.content.value == content, self.data.values()
                    )
                )
            )
        if tags != None:
            res.extend(
                list(
                    filter(
                        lambda record: str(record.tags) == tags,
                        self.data.values(),
                    )
                )
            )

        return res

    def save(self, record: Note):
        title = str(record.title)
        self.data[title] = record
        
    def delete(self, title: str):
        if title in self.data:
            del self.data[title]

    def __str__(self):
        if len(self.data) == 0:
            return("Notes are empty")
        return "\n".join(str(record) for record in self.data.values())

    def show(self):
        if len(self.data) == 0:
            print("Notes are empty")
        for record in self.data.values():
            return(record)  

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
       
    def find_note_by_tag(self, tag):
        found_notes = []
        normalized_tag = tag.strip().lower()  # Нормалізуємо тег до нижнього регістру та видаляємо зайві пробіли
        for title, note in self.data.items():
            normalized_tags = [t.strip().lower() for t in note['tags']]  # Нормалізуємо всі теги нотатки до нижнього регістру
            if normalized_tag in normalized_tags:
                found_notes.append(title)
        return found_notes
