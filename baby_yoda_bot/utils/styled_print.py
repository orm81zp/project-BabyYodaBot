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
    options = {"header_style": "bright_yellow", "min_width": 80}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = (
            options.get("title") or f"⚔️ {str(self.model.id)}'s Note's"
        )

    def print(self):
        table = Table(**self.options)
        table.add_column("Id", min_width=15)
        table.add_column("Content")
        table.add_column("Tags")


        content = self.model.show_content() if len(self.model.show_content())>0 else '-'
        tags = self.model.show_tags() if len(self.model.show_tags())>0  else '-'
        table.add_row(str(self.model.id),content, tags)

        Console().print(table)
        
class PrintNotes(PrintObject):
    options = {"header_style": "bright_red", "min_width": 90}

    def __init__(self, model, options):
        super().__init__(model)
        self.options.update(options)
        self.options["title"] = options.get("title") or "⚔️ All Notes"

    def print(self):
        table = Table(**self.options)
        table.add_column("Id", min_width=15)
        table.add_column("Content")
        table.add_column("Tags")


        notes = self.model.values() if isinstance(self.model, dict) else self.model

        for note in notes:
            content = note.show_content() if len(note.show_content())>0 else '-'
            tags = note.show_tags() if len(note.show_tags())>0  else '-'
            table.add_row(str(note.id),content, tags)
        Console().print(table)


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
        table.add_column("Address")

        table.add_row(
            str(self.model.name),
            self.model.get_phones(),
            str(self.model.birthday),
            str(self.model.email),
            str(self.model.address),
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
        table.add_column("Address")

        contacts = self.model.values() if isinstance(self.model, dict) else self.model

        for contact in contacts:
            table.add_row(
                str(contact.name),
                contact.get_phones(),
                str(contact.birthday),
                str(contact.email),
                str(contact.address),
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
