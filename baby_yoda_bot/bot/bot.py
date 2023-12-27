from baby_yoda_bot.exceptions.exceptions import (
    ValidationValueException,
    UnexpectedException,
)
from baby_yoda_bot.commands.commands import EXIT_COMMANDS, CMD_HELP
from baby_yoda_bot.constants import TEXT
from ..assets import logo, phrase
from .basic_bot import BasicBot


class Bot(BasicBot):
    def welcome(self):
        self.animate(logo)
        print(TEXT["WELCOME"])
        self.exec(CMD_HELP)

    def goodbye(self):
        self.animate(phrase, 0.1)
        print("Goodbye! See you soon...\n")

    def listen(self):
        self.welcome()

        while True:
            try:
                command = self.get_command()

                if command:
                    if command in EXIT_COMMANDS:
                        self.goodbye()
                        break

                    self.exec(command)
                else:
                    self.ask_command()
            except ValidationValueException as err:
                print(err)
            except KeyboardInterrupt:
                print("See you later!")
                self.save()
                break
            except UnexpectedException as err:
                print("Oops! Something went wrong!")
                print(err)

        self.save()


__all__ = ["Bot"]
