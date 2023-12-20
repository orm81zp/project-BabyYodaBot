import re
from .Field import Field
from ..exceptions import ValidationValueException


class Tag(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\w{1,15}$", new_value):
            self.__value = new_value
        else:
            raise ValidationValueException("Tag failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Tag: {self.__value}")
