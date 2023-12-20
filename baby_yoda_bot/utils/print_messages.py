from rich.console import Console
from rich.theme import Theme


def print_diff(old_value, new_value):
    custom_theme = Theme({"old": "grey0", "new": "bright_green"})
    console = Console(theme=custom_theme)
    console.print(f"[old]{old_value}[/] => [new]{new_value}[/]")


def print_message(suffix):
    def inner(prefix):
        print(prefix + " " + suffix)

    return inner


print_updated = print_message("updated!")
print_not_found = print_message("not found!")
print_added = print_message("added!")
print_deleted = print_message("deleted!")
print_exists = print_message("already exists!")

__all__ = [
    "print_diff",
    "print_message",
    "print_updated",
    "print_not_found",
    "print_added",
    "print_deleted",
    "print_exists",
]
