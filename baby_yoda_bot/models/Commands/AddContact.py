from ..Record import Record
from .BaseCommand import BaseCommand


class AddContact(BaseCommand):
    def __init__(self, args):
        super().__init__()
        # example how to add Record
        fields = self.get_fields_by_wizard(
            fields={"name": True, "birthday": False, "phone": False, "email": False}
        )

        record = Record(fields["name"])  # required name
        if fields["birthday"]:
            record.add_birthday(fields["birthday"])  # not required
        if fields["phone"]:
            record.add_phone(fields["phone"])  # not required
        if fields["email"]:
            record.add_address(fields["email"])  # not required

        self.address_book.save(record)

        # ask to add another contact
        if self.is_yes():
            self.add_contact(args)

        # record = Record("Antonina")  # required name
        # record.add_birthday("12.04.1989")  # not required
        # record.add_phone("+380503622500")  # not required
        # record.add_address("antonina@gmail.com")  # not required
        # self.address_book.save(record)
        # self.address_book.show()

        # list_baby_record = self.address_book.find(email="antonina@gmail.com")   # вернет list baby_yoda_bot.models.Record.Record
        # list_baby_record = self.address_book.find(birthday="23.02.1985")   # вернет list baby_yoda_bot.models.Record.Record
        # что бы увидеть результат через цикл:
        # for record in list_baby_record:
        #     print(record)
        # без параметров вызов self.address_book.find() вернет все значения

        # change record:
        # record1 = Record("Antonina")  # required name
        # record1.add_birthday("23.03.1985")  # not required
        # record1.add_phone("+440503622544")  # not required
        # record1.add_address("antoninasych@gmail.com")  # not required
        # self.address_book.save(record1)
        # self.address_book.show()

        self.address_book.save_to_file()  # записую у файл
