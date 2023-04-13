#!/usr/bin/python3
"""Module to convert a JSON string to a Python data structure."""

import json


def from_json_string(my_str: str) -> any:
    """Convert a JSON string to a Python data structure and return it.

    Args:
        my_str: The JSON string to convert.

    Returns:
        The Python data structure represented by the JSON string.
    """
    data = json.loads(my_str)
    return data
