#!/usr/bin/python3
"""This module defines a class Student."""


class Student:

    """
    Represent a student.
    """


def __init__(self, first_name, last_name, age):
    """
    Initializes a new instance of the Student class.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self, attributes=None):
    """
    Returns a dictionary representation of the Student instance.

    If attributes is a list of strings, only the attributes
    included in the list are represented.

    Args:
        attributes (list): (Optional) The attributes to represent.
    """
    if (type(attributes) == list and
            all(isinstance(ele, str) for ele in attributes)):
        return {k: getattr(self, k) for k in attributes if hasattr(self, k)}
    return self.__dict__


def reload_from_json(self, json_data):
    """
    Replaces all attributes of the Student instance.

    Args:
        json_data (dict): The key/value pairs to replace attributes with.
    """
    for key, value in json_data.items():
        setattr(self, key, value)
