#!/usr/bin/python3
"""Defining Square Class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class."""
        super().__init__(size, size, x, y, id)
        