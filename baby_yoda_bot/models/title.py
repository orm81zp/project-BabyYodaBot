from .field import field
from ..exceptions import ValidationValueException


class title(field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 4 and len(new_value) <= 20:
            self.__value = new_value
        else:
            raise ValidationValueException("Title failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Title: {self.__value}")
