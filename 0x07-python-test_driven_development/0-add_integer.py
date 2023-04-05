#!/usr/bin/python3
"""
This script contains a function for integer addition.
"""


def add_integer(a, b=98):
    """
    Returns the integer sum of arguments a and b.

    Arguments:
    a -- An integer or float value.
    b -- An integer or float value. Default is 98.

    Raises:
    TypeError -- If a or b is not a number.

    Returns:
    The integer sum of a and b after typecasting float values to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")
    return int(a) + int(b)
