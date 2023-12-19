import pickle
from .AddressBook import AddressBook
from .Record import Record


class Bot:
    def __init__(self):
        # self.notes  = Notes()
        # self.notes.read_from_file()
        self.address_book = AddressBook()
        self.address_book = self.address_book.read_from_file()

    # робота із адресной книгой
    def command1(self):
        # example how to add Record
        record = Record("Alex")  # required name
        record.add_birthday("23.02.1985")  # not required
        record.add_phone("+380503611576")  # not required
        record.add_address("alex@gmail.com")  # not required
        self.address_book.saveRecord(record)
        # print(self.address_book.show())
        # record = Record('Anton')  # required name
        # record.add_birthday('12.03.1984')  # not required
        # record.add_phone('+380503611576')  # not required
        # record.add_phone('+380503611576') # not required
        # record.add_address("antonina@gmail.com")  # not required
        # self.address_book.save(record)  # save to Book
        #
        # self.address_book.find() # will  return  all contacts
        # print(self.address_book.find()) # to print them you need  to use print method

    # //робота із notes
    def command2(self):
        pass

        # note = self.notes.find_note({'name'='Alex','description'....})
        # note = note.show('teest@gmail.com')
        # note = note.find('tag'='plant')
        # self.notes.save(record)
