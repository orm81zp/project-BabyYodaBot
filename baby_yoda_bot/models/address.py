from ..exceptions import ValidationValueException
from .field import Field
from ..commands.commands import ARG_ADDRESS, VALIDATION_RULES


class Address(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and (5 <= len(new_value) <= 100):
            self.__value = new_value
        else:
            raise ValidationValueException(VALIDATION_RULES[ARG_ADDRESS])

    def __str__(self):
        return self.__value


__all__ = ["Address"]
