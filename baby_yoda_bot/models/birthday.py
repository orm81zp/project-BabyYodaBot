from datetime import datetime
from ..exceptions import ValidationValueException
from .field import Field
from ..commands.commands import ARG_BIRTHDAY, VALIDATION_RULES


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        try:
            birthday = datetime.strptime(new_value, "%d.%m.%Y")
        except ValueError:
            raise ValidationValueException(VALIDATION_RULES[ARG_BIRTHDAY])

        if birthday > datetime.today():
            raise ValidationValueException(
                "Birthday failed validation. The future's date accepted."
            )

        self.__value = birthday

    def __str__(self):
        return (
            self.__value.strftime("%d.%m.%Y") if self.__value != None else "Not defined"
        )
