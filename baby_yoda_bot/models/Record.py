from .Phone import Phone
from .Name import Name
from .Email import Email
from .Birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        self.birthday = None
        self.email = None
        self.address = None

    def add_email(self, email):
        self.email = Email(email)

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone

    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return phone
        raise ValueError("Phone not found")

    def add_birthday(self, birthday: Birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        if len(phone_numbers) == 0:
            phone_numbers = "Not defined"
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}"
