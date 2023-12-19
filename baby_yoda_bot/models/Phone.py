import re
from ..exceptions import ValidationValueException
from .Field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\+?[0-9]{12}", new_value):
            self.__value = new_value
        else:
            raise ValidationValueException("Phone failed validation.")

    def __str__(self):
        return self.__value
