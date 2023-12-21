from ..exceptions import ValidationValueException
from .field import field


class name(field):
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
        return self.__value
