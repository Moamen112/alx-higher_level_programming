#!/usr/bin/python3
"""
This module contains a subclass of list, the MyList class.
"""


class MyList(list):
    """
    A subclass of list that adds a method for printing a sorted list.
    """
    def __init__(self):
        """Initializes the object."""
        super().__init__()

    def print_sorted(self):
        """
        Prints the sorted list in ascending order.

        Returns:
            None
        """
        print(sorted(self))
