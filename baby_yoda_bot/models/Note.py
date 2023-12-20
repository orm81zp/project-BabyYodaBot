import re
import time
from ..exceptions import ValidationValueException
from .Field import Field


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
