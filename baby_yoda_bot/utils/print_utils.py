def print_message(text):
    def inner(name):
        print(+name.capitalize() + " " + text.lower())

    return inner


__all__ = ["print_message"]
