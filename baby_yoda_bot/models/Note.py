import time
from .Content import Content
from .Title import Title
from .Tag import Tag


class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.content = None
        self.tags = []
        self.date_creation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.date_modification = None

    def add_tags(self, tags):
        if tags and isinstance(tags, list):
            for tag in tags:
                for i in self.tags:
                    if str(i) != tag:
                        self.tags.append(Tag(tag))

    def add_content(self, content):
        self.content = Content(content)

    def __str__(self):
        pass


#         TODO реалізувати як у Record  __str__
