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
    "print_message",
    "print_updated",
    "print_not_found",
    "print_added",
    "print_deleted",
    "print_exists",
]
