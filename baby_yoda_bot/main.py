from .exceptions import UnexpectedException, ValidationValueException
from .commands import EXIT_COMMANDS
from .commands import commands_handler
from .constants import TEXT
from .utils import start_work, stop_work


def yoda_say():
    # add welcome message / animation
    # display help
    print(TEXT["WELCOME"])

    # init addressBook
    book = start_work()

    while True:
        try:
            # TODO user_input = call a function to get user input
            # TODO command, args = call a function to parse user_input
            cmd = input(">>> ")
            command, args = (cmd, [])

            if command:
                commands_handler(command, book, args)
                if command in EXIT_COMMANDS:
                    break
            else:
                print('Invalid command. Type "help".')
        except KeyboardInterrupt:
            pass
            # stop working and save book after forced exit.
        except ValidationValueException as err:
            print(err)
        except UnexpectedException as err:
            print(err)

    stop_work(book=book)


__all__ = ["yoda_say"]
