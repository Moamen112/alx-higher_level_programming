#!/usr/bin/python3
"""
Defines a function that adds attributes to objects if possible.
"""


def add_attribute(obj: object, attribute: str, value: any) -> None:
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the attribute to add.
        value (any): The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
