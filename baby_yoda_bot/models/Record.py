from .Phone import Phone
from .Name import Name
from .Email import Email
from .Birthday import Birthday
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
    def __init__(self, name, silent=False):
        self.name = name
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None
        self.silent = silent

    # ----------- EMAIL------------------------------------------------
    def add_email(self, email):
        old_email = self.email
        self.email = email
        if old_email:
            if not self.silent:
                print_diff(str(old_email), email)
                print_updated("Email")
        else:
            if not self.silent:
                print_added("Email")

    def show_email(self):
        print(self.email)

    def remove_email(self):
        if is_yes("Existing email will be deleted, continue?"):
            self.email = None
            if not self.silent:
                print_deleted("Email")

    # ----------- ADDRESS------------------------------------------------
    def add_address(self, address: Address):
        old_address = self.address
        self.address = address
        if old_address:
            if not self.silent:
                print_diff(str(old_address), address)
                print_updated("Address")
        else:
            if not self.silent:
                print_added("Address")

    def show_address(self):
        print(self.address)

    def remove_address(self):
        if is_yes("Existing address will be deleted, continue?"):
            self.address = None
            if not self.silent:
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

    def add_phone(self, number):
        phone = self.find_phone(number)
        if phone:
            if not self.silent:
                print_exists("Phone number")
            return False

        self.phones.append(number)
        if not self.silent:
            print_added("Phone number")
        return True

    def change_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            for index in range(len(self.phones)):
                if str(self.phones[index]) == old_phone:
                    self.phones[index] = Phone(new_phone)
                    if not self.silent:
                        print_diff(old_phone, new_phone)
                        print_updated("Phone number")
                    break

        else:
            print_not_found("Phone number")

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones = list(filter((lambda p: str(p) != phone_number), self.phones))
            if not self.silent:
                print_deleted("Phone number")
            return True

        if not self.silent:
            print_not_found("Phone number")

        return False

    # ----------- BIRTHDAY----------------------------------------------
    def add_birthday(self, birthday):
        old_birthday = self.birthday
        self.birthday = birthday

        if old_birthday:
            if not self.silent:
                print_diff(str(old_birthday), birthday)
                print_updated("Birthday")
        else:
            if not self.silent:
                print_added("Birthday")

    def show_birthday(self):
        print(self.birthday)

    def remove_birthday(self):
        if is_yes("Existing birthday will be deleted, continue?"):
            self.birthday = None
            if not self.silent:
                print_deleted("Email")

    def show(self):
        StyledPrint(self, entity="contact").print()

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        if len(phone_numbers) == 0:
            phone_numbers = "Not defined"
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}, email: {self.email}"
