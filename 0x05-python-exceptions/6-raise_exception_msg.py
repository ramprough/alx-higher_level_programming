#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    This raises a NameError exception with a custom message.

    Parameters:
    message (str): The message to be included in the exception

    Raises:
    NameError: The exception raised with the custom message
    """
    # Raise the NameError with the custom message
    raise NameError(message)
