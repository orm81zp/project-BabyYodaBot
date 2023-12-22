import time
from .content import Content
from .tag import Tag
from ..utils import (
    StyledPrint,
    is_yes,
    print_diff,
    print_updated,
    print_not_found,
    print_added,
    print_deleted,
    print_exists,
)


class Note:
    def __init__(self, uuid, content=None, tags=None):
        self.uuid = uuid
        self.content = content
        self.tags = set()
        self.date_creation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.date_modification = None

        if tags and len(tags) > 0:
            for tag in tags:
                self.tags.add(Tag(tag))

    # ----------- Tags------------------------------------------------
    def add_tag(self, tag):
        if tag:
            self.tags.add(Tag(tag))

    def get_tags(self):
        return (
            ", ".join([str(tag) for tag in self.tags]) if len(self.tags) > 0 else " - "
        )

    def show_tags(self):
        print(self.get_tags())

    def remove_tags(self):
        self.tags = set()

    # # ----------- Content------------------------------------------------
    def add_content(self, content):
        if self.content:
            self.content = content
            print_updated("Content")

    def show_content(self):
        print(str(self.content))

    def remove_content(self):
        self.content = None
        
    def change_content(self, content):
         self.content = Content(content)
        

    def __str__(self):
        return f"#{str(self.uuid)}, {str(self.content)}\nTags: {self.get_tags()}"
