#!/usr/bin/python3
"""Module that defines a Student class with filter."""


class Student:
    """Defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
