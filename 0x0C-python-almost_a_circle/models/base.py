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
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Deserialize a JSON string and return a Python list.

        Args:
            json_str (str): A JSON string representation of
            a list of dictionaries.

        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
def create(cls, **attrs_dict):
    """Instantiate a class with attributes specified in a dictionary.

    Args:
        **attrs_dict (dict): Key/value pairs of
        attributes to initialize the class with.

    Returns:
        A new instance of the class with the specified attributes.
    """
    if attrs_dict and attrs_dict != {}:
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        else:
            new_instance = cls(1)
        new_instance.update(**attrs_dict)
        return new_instance
