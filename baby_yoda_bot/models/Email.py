import re
from ..exceptions import ValidationValueException
from .Field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        pattern = r"\S+@\S+\.\S+"
        if new_value and re.match(pattern, new_value):
            self.__value = new_value
        else:
            raise ValidationValueException("Email failed validation.")

    def __str__(self):
        return f"Email: {self.__value}"
