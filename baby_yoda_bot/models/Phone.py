from ..exceptions import ValidationValueException
from .Field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if len(new_value) == 10 and new_value.isdigit():
            self.__value = new_value
        else:
            raise ValidationValueException("Phone failed validation.")

    def __str__(self):
        return f"Phone: {self.__value}"
