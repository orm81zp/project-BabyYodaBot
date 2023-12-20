import pickle
from .AddressBook import AddressBook
from .Notes import Notes
from .Record import Record
from .Note import Note


class Bot:
    def __init__(self):
        self.notes = Notes()
        self.notes.read_from_file()
        self.address_book = AddressBook()
        self.address_book.read_from_file()

    # робота із адресной книгой
    def command1(self):
        # example how to add Record
        record = Record("Alex")  # required name
        record.add_birthday("23.02.1985")  # not required
        record.add_phone("+380503611576")  # not required
        record.add_address("alex@gmail.com")  # not required

        self.address_book.save(record)
        record = Record("Antonina")  # required name
        record.add_birthday("12.04.1989")  # not required
        record.add_phone("+380503622500")  # not required
        record.add_address("antonina@gmail.com")  # not required
        self.address_book.save(record)
        # self.address_book.show()

        # list_baby_record = self.address_book.find(email="antonina@gmail.com")   # вернет list baby_yoda_bot.models.Record.Record
        # list_baby_record = self.address_book.find(birthday="23.02.1985")   # вернет list baby_yoda_bot.models.Record.Record
        # что бы увидеть результат через цикл:
        # for record in list_baby_record:
        #     print(record)
        # без параметров вызов self.address_book.find() вернет все значения

        # change record:
        record1 = Record("Antonina")  # required name
        record1.add_birthday("23.03.1985")  # not required
        record1.add_phone("+440503622544")  # not required
        record1.add_address("antoninasych@gmail.com")  # not required
        self.address_book.save(record1)
        self.address_book.show()

        self.address_book.save_to_file()  # записую у файл

    # //робота із notes
    def command2(self):
        note = Note("First Note")
        print(note)
        # note.add_content('bla-bla-bla)
        # note.add_tags('tag1','tag2', 'tag2')
        # self.notes.save(note)

        # note = self.notes.find({'id'='1','content'="bla-bla", tag = tag2})
        # self.notes.show()
        # note = note.find('tag'='plant')
        # self.notes.delete(note)
        # self.notes.save(note)
