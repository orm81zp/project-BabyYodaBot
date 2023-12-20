from collections import defaultdict
from baby_yoda_bot.models.AddressBook import AddressBook
from baby_yoda_bot.utils import request_input, parse_input

class Bot:
    __COMMANDS_METADATA__ = defaultdict(dict)

    @staticmethod
    def command(name):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__['map'][name] = func
            print('command', key)

            return inner
        return decorator

    @staticmethod
    def arguments(args):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            Bot.__COMMANDS_METADATA__[key]['args'] = args
            print('arguments', key)

            return inner

        return decorator


    @staticmethod
    def description(description):
        def decorator(func):
            inner, key = Bot.__make_inner(func)
            print('describe', key)
            print('Metadata', Bot.__COMMANDS_METADATA__[key])
            Bot.__COMMANDS_METADATA__[key]['description'] = description

            return inner
        return decorator

    @staticmethod
    def __make_inner(func):
        inner = func
        name = func.__name__

        if hasattr(func, '__bot_cmd__'):
            name = func.__bot_cmd__
        else:
            setattr(inner, '__bot_cmd__', name)

        return inner, name

    def __init__(self):
        # TODO: add save/read from file
        # TODO: add notes class initialization
        self.address_book = AddressBook()

   

__all__ = [
  'Bot'
]