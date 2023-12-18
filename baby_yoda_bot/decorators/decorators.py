def confirm_prompt(message="Please confirm"):
    def handler(func):
        def inner(*args, **kwargs):
            user_input = input(f"{message} (y/no) ")
            user_input = user_input.strip().lower()
            if user_input in ["yes", "y"]:
                return func(*args, **kwargs)

        return inner

    return handler


def input_error(error):
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                print(error)

        return inner

    return error_handler


__all__ = ["input_error", "confirm_prompt"]
