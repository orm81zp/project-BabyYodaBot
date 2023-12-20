from .exceptions import UnexpectedException, ValidationValueException
from .commands import EXIT_COMMANDS
from .commands import commands_handler
from .constants import TEXT
from .models.Bot import Bot

from .bot import Bot

def yoda_say():
    bot = Bot()
    bot.listen()
