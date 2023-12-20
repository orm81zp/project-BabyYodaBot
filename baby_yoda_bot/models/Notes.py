from collections import UserDict
from .Note import Note
from .BasicModel import BasicModel


class Notes(UserDict, BasicModel):
    def __init__(self):
        self.data = dict()
        self.filename = "NotesData.dat"

    def find(self, id=None, contetnt=None, date=None):
        res = list()
        # додаєшь до спииску результати

        return res

    def save(self, note: Note):
        pass
        # id = str(note.id)
        # self.data[id] = note

    def delete(self, id):
        if id in self.data:
            del self.data[id]

    def __str__(self):
        if len(self.data) == 0:
            print("Notes are empty")
        for record in self.data.values():
            print(record)
