from rich.console import Console
from rich.table import Table


class PrintObject:
    def __init__(self, model):
        self.model = model

    def print(self):
        print(self.model)


class PrintRecord(PrintObject):
    options = {"header_style": "bright_green", "min_width": 80}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title") or f"⚔️ {str(self.model.name)}'s Record"
        )

    def print(self):
        table = Table(**self.options)
        table.add_column("Name", min_width=15)
        table.add_column("Phone")
        table.add_column("Birthday")
        table.add_column("Email")

        table.add_row(
            str(self.model.name),
            self.model.get_phones(),
            str(self.model.birthday),
            str(self.model.email),
        )

        Console().print(table)


class PrintRecords(PrintObject):
    options = {"header_style": "bright_green", "min_width": 90}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or "⚔️ All Contacts"

    def print(self):
        table = Table(**self.options)
        table.add_column("Name", min_width=15)
        table.add_column("Phone")
        table.add_column("Birthday")
        table.add_column("Email")

        contacts = self.model.values() if isinstance(self.model, dict) else self.model

        for contact in contacts:
            table.add_row(
                str(contact.name),
                contact.get_phones(),
                str(contact.birthday),
                str(contact.email),
            )
        Console().print(table)


class StyledPrint:
    def __init__(self, model, entity=None, **options):
        self.options = options
        self.model = model
        self.entity = entity
        self.printer = None
        self.setup()

    def setup(self):
        if self.entity == "contact":
            self.printer = PrintRecord(self.model, self.options)
        elif self.entity == "contacts":
            self.printer = PrintRecords(self.model, self.options)

    def print(self):
        if self.printer:
            self.printer.print()
        else:
            print("Nothing to display")


__all__ = ["StyledPrint"]
