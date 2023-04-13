#!/usr/bin/python3
"""Module to convert an object (string) to JSON format."""

import json


def to_json_string(my_obj) -> str:
    """Return the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON format.

    Returns:
        A string containing the JSON representation of the object.
    """
    data = json.dumps(my_obj)
    return data
