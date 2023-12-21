import time
from .content import Content
from .title import Title
from .tag import Tag


class Note:
    def __init__(self, title):
        self.title = Title(title)
        self.content = None
        self.tags = []
        self.date_creation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.date_modification = None

    # ----------- Tags------------------------------------------------
    def add_tags(self, tags):
        self.tags.append(Tag(tags))

    def show_tags(self):
        return self.tags

    def remove_tags(self):
        self.tags = []

    # ----------- Content------------------------------------------------
    def add_content(self, content):
        self.content = Content(content)

    def show_content(self):
        return self.content

    def remove_content(self):
        self.content = None

    # ----------- Content------------------------------------------------

    def add_title(self, title):
        self.title = Title(title)

    def show_title(self):
        return self.title

    def remove_title(self):
        self.title = None

    def __str__(self):
        return f'Title: {str(self.title)}, Content: {str(self.content)}, Tags: {", ".join([str(tag) for tag in self.tags])}'
