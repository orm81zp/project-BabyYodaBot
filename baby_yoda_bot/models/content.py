from .field import Field
from ..exceptions import ValidationValueException


class Content(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data:str):
        if len(data) > 10 and len(data) <= 500:
            self.__value = data
        else:
            raise ValidationValueException("Content failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Content: {self.__value}")
