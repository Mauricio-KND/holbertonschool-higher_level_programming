#!/usr/bin/python3
"""
Module that defines the is_kind_of_class() function.
"""


def is_kind_of_class(obj, a_class):
    """
    True if the object is instance of a class inherited from specified class.
    """
    return isinstance(obj, a_class)
