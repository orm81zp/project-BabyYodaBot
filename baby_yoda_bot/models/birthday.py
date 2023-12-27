from datetime import datetime, date
from ..exceptions import ValidationValueException
from .field import Field
from ..commands.commands import ARG_BIRTHDAY, VALIDATION_RULES


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


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
                "Birthday failed validation. The future's date not accepted."
            )

        # print a message for a specific age range
        diff_days = calculate_age(birthday)
        if diff_days > 150:
            print("I will pretend that I believed you.")
        elif diff_days > 110:
            print("I hope that everyone is in good health, please send my regards.")
        elif diff_days > 90:
            print("I hope that everyone is in good health.")
        elif diff_days > 70:
            print("Respect and help the elderly!")

        self.__value = birthday

    def __str__(self):
        return (
            self.__value.strftime("%d.%m.%Y") if self.__value != None else "Not defined"
        )
