#!/usr/bin/python3
"""
Initializes the save_to_json_file() function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
