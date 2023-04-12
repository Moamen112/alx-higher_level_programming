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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the print() and str() representation of a Rectangle."""
        string_repr = "[" + str(type(self).__name__) + "] "
        string_repr += str(self.__width) + "/" + str(self.__height)
        return string_repr
