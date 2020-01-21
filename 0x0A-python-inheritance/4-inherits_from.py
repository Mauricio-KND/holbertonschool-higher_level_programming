#!/usr/bin/python3
"""
Module that defines the imherits_from() function.
"""


def inherits_from(obj, a_class):
    """
    True if the object is instance of a class inherited from specified class.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
