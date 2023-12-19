from collections import UserDict
import time
import Field


class Content(Field):
    def __init__(self, value=""):
        super().__init__(value)
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 10 and len(new_value) <= 500:
            self._value = new_value
        else:
            raise ValueError("Content failed validation.")

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self._value)


class Title(Field):
    def __init__(self, value=""):
        super().__init__(value)
        self.value = value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 4 and len(new_value) <= 20:
            self._value = new_value
        else:
            raise ValueError("Title failed validation.")

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class Notes(UserDict):
    def __init__(self, title, content):
        self.title = Title(title)
        self.__content = Content(content)
        self.tags = []
        self.DateCreation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.DateModified = None
