#!/usr/bin/python3
"""Module to write a string to a text file."""


def write_file(filename: str = "", text: str = ""):
    """Write a string to a text file and
    return the number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The text string to write to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, mode="w+", encoding="utf-8") as file:
        return file.write(text)
