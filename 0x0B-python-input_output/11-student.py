#!/usr/bin/python3
"""
Defines a class Student.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def to_json(self, attributes=None):
        """Returns a dictionary representation of the Student.

        If attributes is a list of strings, it represents only those attributes
        included in the list.

        Args:
            attributes (list): (Optional) The attributes to represent.
        """
        if isinstance(attributes, list) and all(isinstance(ele, str) for ele in attributes):
            return {k: getattr(self, k) for k in attributes if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replaces all attributes of the Student.

        Args:
            json_data (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json_data.items():
            setattr(self, key, value)
