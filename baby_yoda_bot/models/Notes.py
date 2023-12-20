import pickle
from collections import UserDict
from .Note import Note
from .BasicModel import BasicModel


class Notes(UserDict, BasicModel):
    def __init__(self):
        self.data = dict()
        self.filename = "NotesData.dat"

    # def find_note(self, index):
    #     for note in self.data["notes"]:
    #         if note.uuid == index:
    #             return note
    #     return None
    #
    # def find_note_by_content(self, content):
    #     for note in self.data["notes"]:
    #         if note.value == content:
    #             return note
    #     return None


# def find(self, name=None, birthday=None, email=None):
#      if name is None and birthday is None and email is None:
#          return self.data
#      res = list()
#      if name != None:
#          if name in self.data:
#              res.append(self.data[name])
#      if email != None:
#          res.extend(
#              list(
#                  filter(
#                      lambda record: record.email.value == email, self.data.values()
#                  )
#              )
#          )
#      if birthday != None:
#          res.extend(
#              list(
#                  filter(
#                      lambda record: str(record.birthday) == birthday,
#                      self.data.values(),
#                  )
#              )
#          )
#
#      return res
#
#  def save(self, record: Record):
#      name = str(record.name)
#      self.data[name] = record
#
#  def delete(self, name: str):
#      if name in self.data:
#          del self.data[name]
#
#  def __str__(self):
#      if len(self.data) == 0:
#          print("Address Book is empty")
#      for record in self.data.values():
#          print(record)
#
#  def show(self):
#      if len(self.data) == 0:
#          print("Address Book is empty")
#      for record in self.data.values():
#          print(record)
#
