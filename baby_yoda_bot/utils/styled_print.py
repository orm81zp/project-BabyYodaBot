from rich.console import Console
from rich.table import Table
from ..models.Record import Record


class PrintObject:
    def __init__(self, model):
        self.model = model

    def print(self):
        print(self.model)


class PrintRecord(PrintObject):
    model: Record
    options = {"header_style": "bright_green", "min_width": 80}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)

    def print(self):
        title = self.options.get("title") or f"⚔️ {str(self.model.name)}'s record"
        table = Table("Name", "Phone", "Birthday", "Email", title=title, **self.options)

        table.add_row(
            str(self.model.name),
            self.model.show_phones(),
            str(self.model.birthday),
            str(self.model.email),
        )

        Console().print(table)


class StyledPrint:
    printer: PrintObject

    def __init__(self, model, **options):
        self.options = options
        self.model = model
        self.init()

    def init(self):
        if isinstance(self.model, Record):
            self.printer = PrintRecord(self.model, self.options)
        else:
            self.printer = PrintObject(self.model)

    def print(self):
        self.printer.print()


__all__ = ["StyledPrint"]
