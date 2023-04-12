#!/usr/bin/python3
"""
This module defines a function that returns
a list of an object's available attributes.
"""


def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
        obj (object): The object whose attributes will be listed.

    Returns:
        A list of strings representing the object's available attributes.
    """
    return dir(obj)
