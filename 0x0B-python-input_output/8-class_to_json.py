#!/usr/bin/python3
"""Defines a Python function to convert
a class instance to a JSON object."""


def class_to_json(obj):
    """Convert a simple data structure to a dictionary representation."""
    return obj.__dict__
