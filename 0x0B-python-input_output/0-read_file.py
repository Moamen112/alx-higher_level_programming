#!/usr/bin/python3
"""Module to read a text file."""

def read_file(filename: str = ""):
    """Reads a text file and prints its content to the standard output.
    
    Args:
        file_name (str): The name of the text file to read. Default to empty string.
        
    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file_obj:
        for line in file_obj:
            print(line, end="")
