from .Phone import Phone
from .Name import Name
from .Email import Email
from .Birthday import Birthday

# todo

# add_phone, show_phone, change_phone, remove_phone
# add_email, show_email, remove_email
# add_birthday, show_birthday, remove_birthday
# add_address, show_address, remove_address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        self.birthday = None
        self.email = None
        self.address = None

    # ----------- EMAIL------------------------------------------------
    def add_email(self, email):
        self.email = Email(email)

    def show_email(self):
        return self.email

    def remove_email(self):
        self.email = None

    # ----------- PHONE------------------------------------------------
    def add_phone(self, number):
        self.phones.append(Phone(number))

    def show_phone(self):
        return self.phones

    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return phone
        raise ValueError("Phone not found")

    # ----------- BIRTHDAY----------------------------------------------

    def add_birthday(self, birthday: Birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        if len(phone_numbers) == 0:
            phone_numbers = "Not defined"
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}"
