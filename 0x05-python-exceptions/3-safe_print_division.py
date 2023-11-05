#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
    The result of the division, or None

    Prints:
    The result of the division, or an error message
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
