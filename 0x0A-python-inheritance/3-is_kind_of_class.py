#!/usr/bin/python3
"""
This module defines a function for checking
if an object is an instance or inherited instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a given class.

    Args:
        obj (object): The object to check the class of.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance or
        inherited instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
