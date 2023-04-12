#!/usr/bin/python3
"""
Defines the MyInt class which
inherits from int and inverts == and != operators.
"""


class MyInt(int):
    """
    Represents an integer object with inverted == and != operators.
    """

    def __eq__(self, value: int) -> bool:
        """
        Overrides the == operator with != behavior.

        Args:
            value (int): The value to compare to.

        Returns:
            bool: True if values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value: int) -> bool:
        """
        Overrides the != operator with == behavior.

        Args:
            value (int): The value to compare to.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        return self.real == value
