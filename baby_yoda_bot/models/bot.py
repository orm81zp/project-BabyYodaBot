import pickle
from .address_book import address_book
from .record import record


class bot:
    def __init__(self):
        # self.notes  = Notes()
        # self.notes.read_from_file()
        self.address_book = address_book()
        self.address_book.read_from_file()

    # робота із адресной книгой
    def command1(self):
        # example how to add Record
        record = record("Alex", silent=True)  # required name
        record.add_birthday("23.02.1985")  # not required
        record.add_birthday("24.02.1985")  # not required
        record.add_phone("+380503611576")  # not required
        record.add_email("alex@gmail.com")  # not required

        self.address_book.save(record)
        record = record("Antonina", silent=True)  # required name
        record.add_birthday("12.04.1989")  # not required
        record.add_phone("+380503622500")  # not required
        record.add_email("antonina@gmail.com")  # not required

        self.address_book.save(record)
        # self.address_book.show()

        # list_baby_record = self.address_book.find(email="antonina@gmail.com")   # вернет list baby_yoda_bot.models.Record.Record
        # list_baby_record = self.address_book.find(birthday="23.02.1985")   # вернет list baby_yoda_bot.models.Record.Record
        # что бы увидеть результат через цикл:
        # for record in list_baby_record:
        #     print(record)
        # без параметров вызов self.address_book.find() вернет все значения

        # change record:
        record1 = record("Antonina", silent=True)  # required name
        record1.add_birthday("23.03.1985")  # not required
        record1.add_phone("+440503622544")  # not required
        record1.add_email("antoninasych@gmail.com")  # not required
        self.address_book.save(record1)

        self.address_book.show()

        self.address_book.search("Ale")

        self.address_book.save_to_file()  # записую у файл

    # //робота із notes
    def command2(self):
        pass

        # note = self.notes.find_note({'name'='Alex','description'....})
        # note = note.show('teest@gmail.com')
        # note = note.find('tag'='plant')
        # self.notes.save(record)
