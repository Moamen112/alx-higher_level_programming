#!/usr/bin/python3
"""Defining a class for rectangle."""
from models.base import Base


class Rectangle(Base):
    """A class to represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An optional integer id.

        Attributes:
            width (int): The public instance width attribute.
            height (int): The public instance height attribute.
            x (int): The public instance x attribute.
            y (int): The public instance y attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the private instance width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private instance width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the private instance height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private instance height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the private instance x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the private instance x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the private instance y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the private instance y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
