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

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
