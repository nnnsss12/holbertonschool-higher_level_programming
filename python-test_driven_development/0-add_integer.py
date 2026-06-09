#!/usr/bin/python3
"""
This module provides a function to add two integers.
It validates input types and casts floats to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to int).
    Raises TypeError if inputs are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
