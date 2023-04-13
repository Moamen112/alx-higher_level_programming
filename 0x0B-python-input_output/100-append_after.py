#!/usr/bin/python3
"""
This module contains a function that
appends a string after a given string
in a text file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a string after each line
    containing a given string in a file.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each occurrence of
        search_string in the file.
    """
    file_text = ""
    with open(filename) as f:
        for line in f:
            file_text += line
            if search_string in line:
                file_text += new_string
    with open(filename, "w") as f:
        f.write(file_text)
