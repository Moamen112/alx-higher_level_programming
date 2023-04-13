#!/usr/bin/python3
"""Module to add all arguments to a Python list and save them to a file."""

import sys
from typing import List
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(args: List[str], file_name: str) -> None:
    """Add all arguments to a Python list and save them to a file.

    Args:
        args: The list of command-line arguments to add to the list.
        file_name: The name of the file to save the list to.

    Returns:
        None.
    """
    try:
        my_list = load_from_json_file(file_name)
    except FileNotFoundError:
        my_list = []
    for i, arg in enumerate(args):
        if i > 0:
            my_list.append(arg)
    save_to_json_file(my_list, file_name)


if __name__ == "__main__":
    add_item(sys.argv, "add_item.json")
