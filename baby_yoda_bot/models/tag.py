import re
from .field import Field
from ..exceptions import ValidationValueException
from ..commands.commands import ARG_TAG, VALIDATION_RULES


class Tag(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\w{1,15}$", new_value):
            self.__value = new_value.strip()
        else:
            raise ValidationValueException(
                f"Tag failed validation. {VALIDATION_RULES[ARG_TAG]}"
            )

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Tag: {self.__value}")
