#!/usr/bin/python3
"""Module to append a string to the end of a text file."""


def append_write(filename: str = "", text: str = ""):
    """Append a string to the end of a text file and
    return the number of characters added.

    Args:
        filename: The name of the file to append to.
        text: The text string to append to the file.

    Returns:
        The number of characters added to the file.
    """
    with open(filename, mode="a+", encoding="utf-8") as file:
        return file.write(text)
