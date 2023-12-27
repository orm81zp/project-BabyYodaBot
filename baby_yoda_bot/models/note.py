import time
from .content import Content
from ..utils import (
    print_updated,
    print_not_found,
    print_added,
    print_deleted,
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
                self.tags.add(tag)

    # ----------- Tags------------------------------------------------
    def add_tag(self, tags):
        if tags and len(tags) > 0:
            for tag in tags:
                self.tags.add(tag)

            text = "Tag" if len(tags) == 1 else "Tags"
            print_added(text)

    def get_tags(self):
        return (
            ", ".join([str(tag) for tag in self.tags]) if len(self.tags) > 0 else " - "
        )

    def show_tags(self):
        print(self.get_tags())

    def remove_tag(self, tags):
        if tags and len(tags) > 0:
            count_before = len(self.tags)
            tags = list(map((lambda tag: str(tag)), tags))
            self.tags = set(list(filter((lambda tag: str(tag) not in tags), self.tags)))

            text = "Tag" if len(tags) == 1 else "Tags"
            if count_before > len(self.tags):
                print_deleted(text)
            else:
                print_not_found(text)

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
