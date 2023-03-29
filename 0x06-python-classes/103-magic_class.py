#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self._MagicClass__radius)
