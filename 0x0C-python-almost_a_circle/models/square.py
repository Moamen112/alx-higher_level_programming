#!/usr/bin/python3
"""Defines a class for a square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): An optional integer id.

        Attributes:
            id (int): The public instance id attribute.
            width (int): The public instance width attribute.
            height (int): The public instance height attribute.
            x (int): The public instance x attribute.
            y (int): The public instance y attribute.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

