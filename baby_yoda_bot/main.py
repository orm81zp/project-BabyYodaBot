"""Module providing an entry point to the Bot."""
from .bot import Bot


def yoda_say():
    """
    Calls to launch the Bot. Start the commands listening process.

    No arguments

    Returns None
    """
    bot = Bot()
    bot.listen()
