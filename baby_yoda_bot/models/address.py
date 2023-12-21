from ..exceptions import ValidationValueException
from .field import field


class Address(field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and (10 <= len(new_value) <= 100):
            self.__value = new_value
        else:
            raise ValidationValueException("Address failed validation.")

    def __str__(self):
        return self.__value


__all__ = ["Address"]
