#!/usr/bin/python3
"""
This module defines the Rectangle class which inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
