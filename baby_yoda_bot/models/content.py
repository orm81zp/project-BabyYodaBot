from .field import field
from ..exceptions import ValidationValueException


class content(field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 10 and len(new_value) <= 500:
            self.__value = new_value
        else:
            raise ValidationValueException("Content failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Content: {self.__value}")
