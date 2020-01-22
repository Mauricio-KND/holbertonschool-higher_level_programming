#!/usr/bin/python3
"""
Initializes the Student class.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
