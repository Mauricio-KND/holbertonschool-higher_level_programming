#!/usr/bin/python3
"""Defining Square Class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <width>/<height>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """ Set size. """
        self.width = value
        self.height = value
