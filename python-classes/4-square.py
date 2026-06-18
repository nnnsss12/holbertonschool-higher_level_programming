#!/usr/bin/python3
"""Module that defines a Square class with getter and setter for size."""


class Square:
    """A class that defines a square with property getter and setter."""

    def __init__(self, size=0):
        """Instantiates a Square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
