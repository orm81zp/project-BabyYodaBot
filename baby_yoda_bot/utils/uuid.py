from string import ascii_letters, digits
from random import choices
from time import time


def generate_uuid():
    characters_list = choices(ascii_letters + digits, k=10)
    return "".join(characters_list) + ":" + str(time())


__all__ = ["generate_uuid"]
