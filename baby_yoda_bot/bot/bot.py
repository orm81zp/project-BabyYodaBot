from collections import defaultdict
from baby_yoda_bot.models.AddressBook import AddressBook
from baby_yoda_bot.utils import request_input, parse_input
from baby_yoda_bot.exceptions.exceptions import ValidationValueException

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

    def __exec(self, command, args):
        if command not in Bot.__COMMANDS_METADATA__['map']:
            return f"Unknown '{command}', use help to see commands list"

        executor = Bot.__COMMANDS_METADATA__['map'][command]
        metadata_key = executor.__bot_cmd__
        metadata = Bot.__COMMANDS_METADATA__[metadata_key]

        if metadata['args']:
            if isinstance(metadata['args'], list):
                validated_args = []

                for rule in metadata['args']:
                    is_optional = not rule['required'] if 'required' in rule else False

                    while True:
                        optional = '(optional)' if is_optional else ''
                        value = input(f"Enter {rule['name']}{optional}: ")

                        if not value and is_optional:
                            value = None
                            break

                        if 'type' in rule:
                            try:
                                value = rule['type'](value)
                                break
                            except ValidationValueException as e:
                                print(e)
                                continue
                
                      
                    validated_args.append(value)

                args = validated_args

            if isinstance(metadata['args'], str):
                pass
                # TODO: add args validation just by template like '<name> <phone> <birthday>

        ctx = {
            'address_book': self.address_book
        }

        return executor(ctx, args)

    def listen(self):
        # TODO: add hello message or animation

        while True:
            try:
                command = request_input('Enter command: ')

                if not command:
                    continue

                cmd, *args = parse_input(command)
                output = self.__exec(cmd, args)

                print(output)
            except Exception as e:
                print(e)
                break
            except KeyboardInterrupt:
                print('\nBye!')
                break


__all__ = [
  'Bot'
]