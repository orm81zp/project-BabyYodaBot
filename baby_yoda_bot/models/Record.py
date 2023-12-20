from .Phone import Phone
from .Name import Name
from .Email import Email
from ..utils.styled_print import StyledPrint


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        self.birthday = None
        self.email = None
        self.address = None

    # ----------- EMAIL------------------------------------------------
    def add_address(self, email):
        self.email = Email(email)

    def show_address(self):
        return self.email

    def remove_address(self):
        self.email = None

    # ----------- PHONE------------------------------------------------
    def add_phone(self, number):
        self.phones.append(Phone(number))

    def show_phones(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return phone_numbers

    def change_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if str(self.phones[i]) == old_phone.strip(""):
                self.phones[i] = Phone(new_phone)

    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return phone
        print("Phone not found")

    def remove_phone(self, search_phone):
        try:
            phone = self.find_phone(search_phone)
            self.phones.remove(phone)
        except KeyError:
            print("Phone not found")

    # ----------- BIRTHDAY----------------------------------------------

    def add_birthday(self, birthday):
        self.birthday = birthday

    def show_birthday(self):
        return self.birthday

    def remove_birthday(self):
        self.birthday = None

    def show(self):
        StyledPrint(self, entity="contact").print()

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        if len(phone_numbers) == 0:
            phone_numbers = "Not defined"
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}, email: {self.email}"
