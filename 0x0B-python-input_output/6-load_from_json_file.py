#!/usr/bin/python3
"""Module to create an object from a JSON file."""

import json


def load_from_json_file(filename: str) -> any:
    """Create an object from a JSON file and return it.

    Args:
        filename: The name of the JSON file to load the object from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, mode="r") as file:
        return json.load(file)
