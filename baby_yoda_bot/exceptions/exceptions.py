"""Module providing exception classes."""


class ValidationValueException(Exception):
    """Class is used for validation errors."""


class UnexpectedException(Exception):
    """Class is used for unexpected errors."""


__all__ = ["ValidationValueException", "UnexpectedException"]
