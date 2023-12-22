from ..exceptions import ValidationValueException
from .field import Field
from ..commands.commands import ARG_NAME, VALIDATION_RULES

class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if len(new_value) < 30 and len(new_value) > 1:
            self.__value = new_value
        else:
            raise ValidationValueException(f"Name failed validation. {VALIDATION_RULES[ARG_NAME]}")

    def __str__(self):
        return self.__value
