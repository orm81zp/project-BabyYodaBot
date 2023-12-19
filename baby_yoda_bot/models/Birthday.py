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
            self.__value = datetime.strptime(new_value, "%d.%m.%Y")
        except ValueError:
            raise ValidationValueException("Birthday failed validation.")

    def __str__(self):
        return f"Birthday: {self.__value.strftime('%d.%m.%Y')}"
