from .phone import Phone
from .name import Name
from .email import Email
from .birthday import Birthday
from .address import Address
from ..utils import (
    StyledPrint,
    is_yes,
    print_diff,
    print_updated,
    print_not_found,
    print_added,
    print_deleted,
    print_exists,
)


class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        self.address = address

        if phone:
            self.phones.append(phone)

    # ----------- EMAIL------------------------------------------------
    def add_email(self, email):
        old_email = self.email
        self.email = email
        if old_email:
            print_diff(str(old_email), email)
            print_updated("Email")
        else:
            print_added("Email")

    def show_email(self):
        email = str(self.email) if self.email else " - "
        print(email)

    def remove_email(self):
        if is_yes("Existing email will be deleted, continue?"):
            self.email = None
            print_deleted("Email")

    # ----------- ADDRESS------------------------------------------------
    def add_address(self, address: Address):
        old_address = self.address
        self.address = address
        if old_address:
            print_diff(str(old_address), address)
            print_updated("Address")
        else:
            print_added("Address")

    def show_address(self):
        address = str(self.address) if self.address else " - "
        print(address)

    def remove_address(self):
        if is_yes("Existing address will be deleted, continue?"):
            self.address = None
            print_deleted("Address")

    # ----------- PHONE------------------------------------------------
    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return phone
        return None

    def get_phones(self, placeholder=" - "):
        phone_numbers = placeholder
        if len(self.phones) > 0:
            phone_numbers = ", ".join([str(phone) for phone in self.phones])

        return phone_numbers

    def show_phone(self):
        print(self.get_phones())

    def add_phone(self, number):
        phone = self.find_phone(number)
        if phone:
            print_exists("Phone number")
            return False

        self.phones.append(Phone(number))
        print_added("Phone number")
        return True

    def change_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            for index in range(len(self.phones)):
                if str(self.phones[index]) == old_phone:
                    self.phones[index] = Phone(new_phone)
                    print_updated("Phone number")
                    return True
        else:
            print_not_found("Phone number {old_phone}")
            return False

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones = list(filter((lambda p: str(p) != phone_number), self.phones))
            print_deleted("Phone number")
            return True

        print_not_found("Phone number")
        return False

    # ----------- BIRTHDAY----------------------------------------------
    def add_birthday(self, birthday):
        old_birthday = self.birthday
        self.birthday = birthday

        if old_birthday:
            print_diff(str(old_birthday), birthday)
            print_updated("Birthday")
        else:
            print_added("Birthday")

    def show_birthday(self):
        birthday = str(self.birthday) if self.birthday else " - "
        print(birthday)

    def remove_birthday(self):
        if is_yes("Existing birthday will be deleted, continue?"):
            self.birthday = None
            print_deleted("Birthday")

    def show(self):
        StyledPrint(self, entity="contact").print()

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        if len(phone_numbers) == 0:
            phone_numbers = "Not defined"
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}, email: {self.email}"
