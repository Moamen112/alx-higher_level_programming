#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """An init method for class Square.

        Args:
            size (int): An integer varibale.
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
