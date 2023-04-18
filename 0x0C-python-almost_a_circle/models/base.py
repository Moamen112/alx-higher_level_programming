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

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from
        a JSON file with the same name as the class.

        Returns:
            A list of objects instantiated from the JSON file.

        If the file does not exist or cannot be opened,
        an empty list is returned.
    """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**attrs_dict) for attrs_dict in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, object_list):
        """Write a list of objects to a CSV file in the format of the class.

        Args:
            object_list (list): A list of objects of the current class.

        Writes to a file named `<cls.__name__>.csv`.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if object_list is None or object_list == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in object_list:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of objects instantiated
        from a CSV file of the class.

        Reads from a file named `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated objects.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in dict_reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turtle_instance = turtle.Turtle()
        turtle_instance.screen.bgcolor("#b7312c")
        turtle_instance.pensize(3)
        turtle_instance.shape("turtle")

        turtle_instance.color("#ffffff")
        for rectangle in list_rectangles:
            turtle_instance.showturtle()
            turtle_instance.up()
            turtle_instance.goto(rectangle.x, rectangle.y)
            turtle_instance.down()
            for i in range(2):
                turtle_instance.forward(rectangle.width)
                turtle_instance.left(90)
                turtle_instance.forward(rectangle.height)
                turtle_instance.left(90)
            turtle_instance.hideturtle()

        turtle_instance.color("#b5e3d8")
        for square in list_squares:
            turtle_instance.showturtle()
            turtle_instance.up()
            turtle_instance.goto(square.x, square.y)
            turtle_instance.down()
            for i in range(2):
                turtle_instance.forward(square.width)
                turtle_instance.left(90)
                turtle_instance.forward(square.height)
                turtle_instance.left(90)
            turtle_instance.hideturtle()

        turtle.exitonclick()
