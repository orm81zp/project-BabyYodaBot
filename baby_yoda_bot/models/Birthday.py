import re
from datetime import datetime
from ..exceptions import ValidationValueException
from .Field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        try:
            birthday = datetime.strptime(new_value, "%d.%m.%Y")
        except ValueError:
            raise ValidationValueException("Birthday failed validation.")

        # check that the birthday is not in the future
        if birthday > datetime.today():
            raise ValidationValueException(
                "Birthday failed validation. The future's date of birth is not accepted."
            )

        self._value = birthday

    def __str__(self):
        return f"Birthday: {self.__value}"
