from rich.console import Console
from rich.table import Table
from ..models import Birthday, Record


class PrintObject:
    def __init__(self, model, **options):
        self.model = model
        self.options = options

    def print(self):
        print(self.model)


class PrintBirthday(PrintObject):
    model: Birthday

    def print(self):
        title = self.options["title"] if "title" in self.options else "Birthday"
        table = Table(title=title)
        table.add_column("Date", style="cyan")
        table.add_row(str(self.model))
        Console().print(table)


class PrintRecord(PrintObject):
    model: Record

    def print(self):
        title = (
            self.options["title"]
            if "title" in self.options
            else f"Contact record of {str(self.model.name)}"
        )
        table = Table(title=title)
        table.add_column("Name")
        table.add_column("Phone")
        table.add_column("Birthday")
        table.add_column("Email")

        phones = (
            ", ".join(str(phone) for phone in self.model.phones)
            if len(self.model.phones)
            else "--"
        )
        table.add_row(
            str(self.model.name),
            phones,
            str(self.model.birthday),
            str(self.model.email),
        )

        Console().print(table)


class PrintModel:
    printer: PrintObject

    def __init__(self, model, **options):
        self.options = options
        self.model = model
        self.init()

    def init(self):
        if isinstance(self.model, Birthday):
            self.printer = PrintBirthday(self.model, **self.options)
        elif isinstance(self.model, Record):
            self.printer = PrintRecord(self.model, **self.options)
        else:
            self.printer = PrintObject(self.model, **self.options)

    def print(self):
        self.printer.print()
