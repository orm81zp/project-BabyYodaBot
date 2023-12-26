from random import choice
from baby_yoda_bot.exceptions.exceptions import (
    ValidationValueException,
    UnexpectedException,
)
from baby_yoda_bot.commands.commands import (
    EXIT_COMMANDS,
    CMD_HELP,
)
from baby_yoda_bot.constants import TEXT
from ..assets import logo, phrase
from .basic_bot import BasicBot


class Bot(BasicBot):
    def welcome(self):
        self.animate(logo)
        print(TEXT["WELCOME"])
        self.exec(CMD_HELP)

    def enter_command(self):
        phrases = [
            'Please, say something... Type "help" to see a hint.',
            'Sorry, I don\'t understand you! Say something! Type "help" to see a hint.',
            'I need more information, I can\'t guess. Type "help" to see a hint.',
            'You must be joking, you didn\'t say anything. Type "help" to see a hint.',
        ]
        print(choice(phrases))

    def listen(self):
        self.welcome()

        while True:
            try:
                user_input = self.request_user_input()
                command = self.parse_user_input(user_input)

                if command:
                    if command in EXIT_COMMANDS:
                        self.animate(phrase, 0.1)
                        print("Goodbye! See you soon...\n")
                        break

                    if self.command_not_found(command):
                        continue

                    self.exec(command)
                else:
                    self.enter_command()
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
