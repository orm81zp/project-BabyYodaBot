import re
from ..exceptions import ValidationValueException
from .field import Field
from ..commands.commands import ARG_EMAIL, VALIDATION_RULES


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        pattern = r"^[a-zA-Z]{1}[a-zA-Z0-9_\.-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        if new_value and re.match(pattern, new_value):
            self.__value = new_value
        else:
            raise ValidationValueException(
                f"Email failed validation. {VALIDATION_RULES[ARG_EMAIL]}"
            )

    def __str__(self):
        return self.__value
