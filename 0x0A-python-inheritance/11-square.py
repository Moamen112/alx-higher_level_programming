#!/usr/bin/python3
"""
This module defines the Square class which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square using the Rectangle class.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
