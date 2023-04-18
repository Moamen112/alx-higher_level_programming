#!/usr/bin/python3
"""Defines a class for a square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.

        Attributes:
            size (int): The size of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return the dictionary representation for the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of a Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
