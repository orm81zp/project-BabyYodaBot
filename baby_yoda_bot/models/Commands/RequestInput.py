from .BaseCommand import BaseCommand


class RequestInput(BaseCommand):
    def __init__(self):
        super().__init__()
        self.name = "RequestInput"
        self.value = self.parse_input(self.request_input("Enter a command: "))
