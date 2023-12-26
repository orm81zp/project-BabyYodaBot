"""Module providing functions for printing models in tables."""
from rich.console import Console
from rich.table import Table


class PrintObject:
    def __init__(self, model):
        self.model = model

    def show(self, value):
        return str(value) if value else " - "

    def print(self):
        print(self.model)


class PrintNote(PrintObject):
    options = {"header_style": "bright_yellow", "min_width": 105}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title") or f":crossed_swords: {str(self.model.uuid)}'s Note"
        )

    def print(self):
        print()
        table = Table(**self.options)
        table.add_column("Id", min_width=10)
        table.add_column("Content", max_width=80)
        table.add_column("Tags")

        table.add_row(
            str(self.model.uuid), self.show(self.model.content), self.model.get_tags()
        )

        Console().print(table)
        print()


class PrintNotes(PrintObject):
    options = {"header_style": "bright_red", "min_width": 105}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or ":crossed_swords: All Notes"

    def print(self):
        print()
        table = Table(**self.options)
        table.add_column("Id", min_width=10)
        table.add_column("Content", max_width=80)
        table.add_column("Tags")

        notes = self.model.values() if isinstance(self.model, dict) else self.model

        for note in notes:
            table.add_row(str(note.uuid), self.show(note.content), note.get_tags())
        Console().print(table)
        print()


class PrintRecord(PrintObject):
    options = {"header_style": "bright_green", "min_width": 105}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title") or f"⚔️ {str(self.model.name)}'s Record"
        )

    def print(self):
        print()
        table = Table(**self.options)
        table.add_column("Name", min_width=15)
        table.add_column("Phone")
        table.add_column("Birthday")
        table.add_column("Email")
        table.add_column("Address")

        table.add_row(
            str(self.model.name),
            self.model.get_phones(),
            self.show(self.model.birthday),
            self.show(self.model.email),
            self.show(self.model.address),
        )

        Console().print(table)
        print()


class PrintRecords(PrintObject):
    options = {"header_style": "bright_green", "min_width": 105}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or ":crossed_swords: All Contacts"

    def print(self):
        print()
        table = Table(**self.options)
        table.add_column("Name", min_width=15)
        table.add_column("Phone")
        table.add_column("Birthday")
        table.add_column("Email")
        table.add_column("Address")

        contacts = self.model.values() if isinstance(self.model, dict) else self.model

        for contact in contacts:
            table.add_row(
                str(contact.name),
                contact.get_phones(),
                self.show(contact.birthday),
                self.show(contact.email),
                self.show(contact.address),
            )
        Console().print(table)
        print()


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
        elif self.entity == "note":
            self.printer = PrintNote(self.model, self.options)
        elif self.entity == "notes":
            self.printer = PrintNotes(self.model, self.options)

    def print(self):
        if self.printer:
            self.printer.print()
        else:
            print("Nothing to display")


__all__ = ["StyledPrint"]
