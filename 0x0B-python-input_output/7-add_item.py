#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves it to a file as JSON.
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    # Name of the file to save the list
    file_name = "add_item.json"

    # Initialize an empty list
    my_list = []

    # Check if the file exists, and load the list if it does
    if path.exists(file_name):
        my_list = load_from_json_file(file_name)

    # Append all arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the list to the file
    save_to_json_file(my_list, file_name)
