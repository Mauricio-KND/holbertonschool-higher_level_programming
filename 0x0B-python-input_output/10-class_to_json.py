#!/usr/bin/python3
"""
Initializes class_to_json() function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure.
    """
    return obj.__dict__
