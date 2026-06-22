#!/usr/bin/python3
"""Module that defines a Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square with [Square] string representation."""

    def __init__(self, size):
        """Instantiates a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
