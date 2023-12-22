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
    def __init__(self, id, silent=False):
        self.id = id
        self.content = None
        self.tags = set()
        self.date_creation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.date_modification = None
        self.silent = silent

    # ----------- Tags------------------------------------------------
    def add_tag(self, tag: str):
        if len(tag) > 0:
            self.tags.add(Tag(tag))
            print_added("Tag")
        else:
            print_updated("Tag")

    def show_tags(self):
        return (
            ", ".join([str(tag) for tag in self.tags]) if len(self.tags) > 0 else " - "
        )

    def remove_tags(self):
        self.tags = []

    # # ----------- Content------------------------------------------------
    def add_content(self, content):
        self.content = Content(content)

    def show_content(self):
        return str(self.content)

    def remove_content(self):
        self.content = None

    # # ----------- Content------------------------------------------------

    # def __str__(self):
    #     return f'Id: {str(self.id)}, Content: {str(self.content)}, Tags: {", ".join([str(tag) for tag in self.tags])}'
