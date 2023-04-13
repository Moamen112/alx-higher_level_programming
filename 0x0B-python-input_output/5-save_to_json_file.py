#!/usr/bin/python3
"""Module to write an object to a text file using JSON format."""

import json


def save_to_json_file(my_obj: any, filename: str) -> None:
    """Write an object to a text file using JSON format.

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file to write the object to.
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
