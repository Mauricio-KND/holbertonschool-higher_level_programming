#!/usr/bin/python3
"""
Module that define a class.
"""


class MyList(list):
    """
    Class MyList
    """
    def print_sorted(self):
        """
         Function that prints a list, sorted (ascending sort).
        """
        print(sorted(self))
