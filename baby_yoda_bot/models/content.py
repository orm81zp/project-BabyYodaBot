from .field import Field
from ..exceptions import ValidationValueException
from ..commands.commands import ARG_CONTENT, VALIDATION_RULES


class Content(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data: str):
        if len(data) > 10 and len(data) <= 500:
            self.__value = data.strip()
        else:
            raise ValidationValueException(VALIDATION_RULES[ARG_CONTENT])

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Content: {self.__value}")
