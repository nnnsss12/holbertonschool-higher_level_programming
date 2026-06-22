#!/usr/bin/env python3
"""Module that defines VerboseList class extending Python list."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Adds item and prints notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends list and prints notification."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Prints notification and removes item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification and pops item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
