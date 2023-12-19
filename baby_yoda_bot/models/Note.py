import re
import time
from ..exceptions import ValidationValueException
from .Field import Field


class Content(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 10 and len(new_value) <= 500:
            self.__value = new_value
        else:
            raise ValidationValueException("Content failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Content: {self.__value}")


class Title(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 4 and len(new_value) <= 20:
            self.__value = new_value
        else:
            raise ValidationValueException("Title failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Title: {self.__value}")


class Tag(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\w{1,15}$", new_value):
            self.__value = new_value
        else:
            raise ValidationValueException("Tag failed validation.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(f"Tag: {self.__value}")


class Note:
    def __init__(self, title, content, tags):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = []
        self.DateCreation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.DateModified = None
        self.add_tags(tags)

    def add_tags(self, tags):
        if tags and isinstance(tags, list):
            for tag in tags:
                for i in self.tags:
                    if str(i) != tag:
                        self.tags.append(Tag(tag))
