"""Module providing different utils."""


def is_yes(msg="Do you want to continue?"):
    """
    Calls to ask a confirmation with providing yes or no choices.

    Parameters:
        msg (str): message

    Returns bool.
    """
    user_input = input(f"{msg} (y/no) ")
    user_input = user_input.strip().lower()

    return user_input in ["yes", "y"]


__all__ = ["is_yes"]
