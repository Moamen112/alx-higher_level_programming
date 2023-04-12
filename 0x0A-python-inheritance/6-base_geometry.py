#!/usr/bin/python3
"""
This module defines the BaseGeometry class,
which represents base geometry.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        Raises:
            Exception: If the area calculation
            is not implemented for the current shape.

        Returns:
            float: The calculated area of the shape.
        """
        raise Exception("area() is not implemented")
