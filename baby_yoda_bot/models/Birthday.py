import re
import datetime
from ..exceptions import ValidationValueException
from .Field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        # check format DD.MM.YYYY
        if not new_value or not re.search(r"^\d{2}\.\d{2}\.\d{4}$", new_value):
            raise ValidationValueException("Birthday failed validation.")

        # check validation on correct day, month, year arguments
        try:
            day, month, year = new_value.split(".")
            birthday_date = datetime.date(
                year=int(year), month=int(month), day=int(day)
            )
        except Exception:
            raise ValidationValueException("Birthday failed validation.")

        # check that the birthday is not in the future
        if birthday_date > datetime.date.today():
            raise ValidationValueException(
                "Birthday failed validation. The future's date of birth is not accepted"
            )

        self._value = new_value

    def __str__(self):
        return f"Birthday: {self.__value}"
