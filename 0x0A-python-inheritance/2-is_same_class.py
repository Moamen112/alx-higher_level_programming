#!/usr/bin/python3
"""
This module defines a function for checking
if an object is an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.

    Args:
        obj (object): The object to check the class of.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
