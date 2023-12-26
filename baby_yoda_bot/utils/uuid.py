"""Module providing functions related to uuid."""
from string import ascii_letters, digits
from random import choices
from time import time


def generate_uuid():
    """
    Calls to generate a random string with datetime.

    No arguments.

    Returns str.
    """
    characters_list = choices(ascii_letters + digits, k=10)
    return "".join(characters_list) + ":" + str(time())


__all__ = ["generate_uuid"]
