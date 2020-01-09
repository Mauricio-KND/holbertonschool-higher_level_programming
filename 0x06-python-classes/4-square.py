#!/usr/bin/python3
"""Module that creates an empty square."""
class Square:
    """Empty square."""
    def __init__(self, size=0):
        """Initialize square with size."""
        self.__size = size
    def area(self):
        """Initialize the current square area."""
        return self.__size * self.__size
    @property
    def size(self):
        """Retrive the square's size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set the square's size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
