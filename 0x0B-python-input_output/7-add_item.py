#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        data = load_json("add_item.json")
    except FileNotFoundError:
        data = []
    data.extend(sys.argv[1:])
    save_json(data, "add_item.json")
