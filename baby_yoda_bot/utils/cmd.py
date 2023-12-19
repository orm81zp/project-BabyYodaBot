def request_input(message = ">>>"):
    """
    Function to request user's input by cmd line.

    Args:
        message (str): Message before input, default value is >>>.

    Returns:
        user input string
    """
    return input(message)


def parse_input(user_input):
    """
    Function to parse user input and split into command and args parts.

    Args:
        user_input (str): User input string.

    Returns:
        command (str): Command part of user input.
        args (list): List of arguments part of user input.
    """
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()

    return cmd, *args

__all__ = [
    'request_input',
    'parse_input'
]
