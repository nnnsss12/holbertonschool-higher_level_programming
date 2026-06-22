#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square inheriting from Rectangle."""

    def __init__(self, size):
        """Instantiates a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
