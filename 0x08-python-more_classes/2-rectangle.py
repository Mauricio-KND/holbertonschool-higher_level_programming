#!/usr/bin/python3
"""
Module that defines a class.
"""


class Rectangle:
    """
    Class Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.
        Arguments:
            width: An integer.
            height: An integer.
        """

        self.width = width
        self.height = height

    @property
    def widht(self):
        """Retrieve the widht"""
        return self.__width

    @widht.setter
    def width(self, value):
        """Set the widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Retrieve the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.area() == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
