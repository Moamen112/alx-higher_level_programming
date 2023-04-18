#!/usr/bin/python3

"""Defines a base model code class."""
import json
import csv
import turtle


class Base:
    """A class to manage the id attribute in all future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): An optional integer id.

        Attributes:
            id (int): The public instance id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_str)
