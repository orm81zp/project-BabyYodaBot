def is_yes(msg="Do you want to continue?"):
    user_input = input(f"{msg} (y/no) ")
    user_input = user_input.strip().lower()

    return user_input in ["yes", "y"]


__all__ = ["is_yes"]
