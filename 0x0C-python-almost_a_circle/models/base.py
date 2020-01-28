#!/usr/bin/python3
"""Defining Base Class."""

import json


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a given list of dictionaries to a json string."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs."""
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(cls.__name__ + ".json", "w") as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        test = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        test.update(**dictionary)
        return test
