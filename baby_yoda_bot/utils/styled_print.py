from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table


class PrintObject(ABC):
    def __init__(self, model):
        self.model = model

    def show(self, value):
        return str(value) if value else " - "

    @abstractmethod
    def print(self):
        pass


class NoteTable(PrintObject):
    options = {"header_style": "bright_red", "min_width": 105}

    def __init__(self, model, **options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title") or f":crossed_swords: {str(self.model.uuid)}'s note"
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


class NotesTable(PrintObject):
    options = {"header_style": "bright_red", "min_width": 105}

    def __init__(self, model, **options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or ":crossed_swords: All notes"

    def print(self):
        print()
        table = Table(**self.options)
        table.add_column("Id", min_width=10)
        table.add_column("Content", max_width=80)
        table.add_column("Created")
        table.add_column("Modified")
        table.add_column("Tags")

        notes = self.model.values() if isinstance(self.model, dict) else self.model

        for note in notes:
            table.add_row(
                str(note.uuid),
                self.show(note.content),
                note.date_creation,
                self.show(note.date_modification),
                note.get_tags(),
            )
        Console().print(table)
        print()


class ContactTable(PrintObject):
    options = {"header_style": "bright_green", "min_width": 105}

    def __init__(self, model, **options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title")
            or f":crossed_swords: {str(self.model.name)}'s contact details"
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


class ContactsTable(PrintObject):
    options = {"header_style": "bright_green", "min_width": 105}

    def __init__(self, model, **options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or ":crossed_swords: All сontacts"

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
    printer: PrintObject

    def __init__(self, printer):
        self.printer = printer

    def print(self):
        self.printer.print()


__all__ = ["StyledPrint", "NoteTable", "NotesTable", "ContactTable", "ContactsTable"]
