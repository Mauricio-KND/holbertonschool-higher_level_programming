#!/usr/bin/python3
"""
Initializes the read_file() function.
"""


def read_file(filename=""):
    """
    Reads a text file (UT8) and print it to stdout.
    """
    with open(filename) as NewText:
        print(NewText.read())
