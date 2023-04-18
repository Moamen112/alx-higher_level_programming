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
        """Width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """X getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""

        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character '#'."""
        # Print y number of new lines before the rectangle
        for i in range(self.y):
            print()
        # Print the rectangle row by row
        for i in range(self.height):
            # Print x number of spaces before the '#' characters in each row
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of a Rectangle instance"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of the Rectangle instance"""

        if len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

     def to_dictionary(self):
        """Return the dictionary representation for the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
