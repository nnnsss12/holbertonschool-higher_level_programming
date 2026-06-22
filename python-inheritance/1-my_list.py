#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """A class that inherits from list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order without modifying it."""
        print(sorted(self))
