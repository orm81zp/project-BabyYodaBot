from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def request_input(message=">>>", compeltions=None):
    """
    Function to request user's input by cmd line.

    Args:
        message (str): Message before input, default value is >>>.
        completions (list): Optional completion list for input

    Returns:
        user input string
    """
    if compeltions:
        return prompt(
            message,
            completer=WordCompleter(compeltions, ignore_case=True, sentence=True),
        )

    return input(message)


def parse_input(user_input):
    """
    Function to parse user input and split into command.

    Args:
        user_input (str): User input string.

    Returns:
        command (str): Command part of user input.
    """
    cmd = user_input.strip().lower()

    return cmd


__all__ = ["request_input", "parse_input"]
