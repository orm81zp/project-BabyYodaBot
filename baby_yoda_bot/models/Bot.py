import pickle
from .AddressBook import AddressBook


class Bot:
    def __init__(self):
        # self.__notes  = Notes()
        # self.notes.read_from_file()
        self.address_book = AddressBook()
        self.address_book = self.address_book.read_from_file()

    def command1(self):
        pass

        # record = self.address_book.find_record({'name'='Alex', 'phone'=>'123456890','email'=>'amy@gmail.com'})
        # record = record.add_address('teest@gmail.com')
        # record = record.remove_phone('2345678')
        # self.address_book.save_record(record)
