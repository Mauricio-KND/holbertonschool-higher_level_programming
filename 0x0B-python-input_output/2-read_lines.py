#!/usr/bin/python3
"""
Initializes the read_lines() function.
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file and prints it to stdout.
    """
    with open(filename) as TextLines:
        if nb_lines <= 0:
            print(TextLines.read(), end="")
            return
        count = 0
        for count, line in enumerate(TextLines):
            if count == nb_lines:
                break
            print(line, end="")
