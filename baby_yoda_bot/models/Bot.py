from .AddressBook import AddressBook
from .Record import Record


def request_input(message=">>> ", required=False):
    user_input = ""
    while True:
        user_input = input(message)

        if required:
            if user_input:
                break
        else:
            break

    return user_input


def parse_input(user_input):
    cmd, *args = user_input.strip().split(" ")
    cmd = cmd.strip().lower()

    return cmd, args


def is_yes():
    user_input = request_input("Want to add another contact? (y/no)")
    user_input = user_input.strip().lower()

    return user_input in ["yes", "y"]


class Bot:
    def __init__(self):
        # self.notes  = Notes()
        # self.notes.read_from_file()
        self.address_book = AddressBook()
        self.address_book.read_from_file()

    def start(self):
        while True:
            try:
                user_input = request_input("Enter a command: ")
                cmd, args = parse_input(user_input)

                if cmd:
                    if cmd == "add-contact":
                        self.add_contact(args)
                    elif cmd == "all-contacts":
                        self.show_all()
                    elif cmd == "help":
                        self.show_help()
                    elif cmd in ["exit", "close"]:
                        print("Bye!")
                        break
                    else:
                        print('Invalid command. Type "help" to see a hint.')
                else:
                    print("Please tell me something :(")
            except Exception as err:
                print(err)

    def get_fields_by_wizard(self, fields: dict[str, bool]):
        filled_fields = {}

        while len(fields) != len(filled_fields):
            for field_name, required in fields.items():
                prompt_string = f"Please enter {field_name.capitalize()}"
                if required:
                    prompt_string += "*"

                prompt_string += " "

                if field_name not in filled_fields:
                    user_input = request_input(prompt_string, required)
                    if required and user_input:
                        filled_fields[field_name] = user_input
                    else:
                        filled_fields[field_name] = user_input or None

        return filled_fields

    # робота із адресной книгой
    def add_contact(self, args):
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
        if is_yes():
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

    def show_help(self):
        print('I can run only "add-contact", "all-contacts" or "exit"')

    # //робота із notes
    def show_all(self):
        self.address_book.show()

        # note = self.notes.find_note({'name'='Alex','description'....})
        # note = note.show('teest@gmail.com')
        # note = note.find('tag'='plant')
        # self.notes.save(record)
