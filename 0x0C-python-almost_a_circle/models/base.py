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
