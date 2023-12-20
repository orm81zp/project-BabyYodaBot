from ..AddressBook import AddressBook


class BaseCommand:
    def __init__(self):
        # self.notes  = Notes()
        # self.notes.read_from_file()
        self.address_book = AddressBook()
        self.address_book.read_from_file()
        # робота із адресной книгой

    def get_fields_by_wizard(self, fields: dict[str, bool]):
        filled_fields = {}

        while len(fields) != len(filled_fields):
            for field_name, required in fields.items():
                prompt_string = f"Please enter {field_name.capitalize()}"
                if required:
                    prompt_string += "*"

                prompt_string += " "

                if field_name not in filled_fields:
                    user_input = self.request_input(prompt_string, required)
                    if required and user_input:
                        filled_fields[field_name] = user_input
                    else:
                        filled_fields[field_name] = user_input or None

        return filled_fields

    def request_input(self, message=">>> ", required=False):
        user_input = ""
        while True:
            user_input = input(message)

            if required:
                if user_input:
                    break
            else:
                break

        return user_input

    def parse_input(self, user_input):
        cmd, *args = user_input.strip().split(" ")
        cmd = cmd.strip().lower()

        return cmd, args

    def is_yes(self):
        user_input = self.request_input("Want to add another contact? (y/no)")
        user_input = user_input.strip().lower()

        return user_input in ["yes", "y"]
