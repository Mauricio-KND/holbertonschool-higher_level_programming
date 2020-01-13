#!/usr/bin/python3
"""
Module for print_square() function.
"""


def print_square(size):
    """Prints a square with the character #.
    Args:
        Size: size length of the square
    Raises:
        TypeError: If argument is not an integer.
        ValueError: If argument is less than 0.
        TypeError: If argument is a float and is less than 0.

    Returns:
        Nothing.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print('#', end='')
        print()
