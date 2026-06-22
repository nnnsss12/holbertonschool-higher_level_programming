#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle using BaseGeometry validation."""

    def __init__(self, width, height):
        """Instantiates a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
