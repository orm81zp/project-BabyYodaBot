import time
from .content import content
from .title import title
from .tag import tag


class note:
    def __init__(self, title):
        self.title = title(title)
        self.content = None
        self.tags = []
        self.date_creation = time.strftime("%Y-%m-%d %H:%M:%S")
        self.date_modification = None
    
     # ----------- Tags------------------------------------------------
    def add_tags(self, tags):
        self.tags.append(tag(tags))
    
    def show_tags(self):
        return self.tags
    
    def remove_tags(self):
        self.tags = None

    
     # ----------- Content------------------------------------------------
    def add_content(self, content):
        self.content = content(content)

    def show_content(self):
        return self.content
    
    def remove_content(self):
        self.content = None

    # ----------- Content------------------------------------------------
        
    def add_title(self,title):
        self.title = title(title)

    def show_title(self):
        return self.title
    
    def remove_title(self):
        self.title = None
   
    def __str__(self):
        return f"Title: {self.title.value}, Content: {content}, Tags: {self.tags.value}"
        

