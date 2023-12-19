from ..exceptions import ValidationValueException
from ..models.Field import Field


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if len(new_value) < 30 and len(new_value) > 1:
            self.__value = new_value
        else:
            raise ValidationValueException("Name failed validation.")

    def __str__(self):
        return f"Name: {self.__value}"
