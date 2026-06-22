#!/usr/bin/env python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """A mixin that provides swimming ability."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying ability."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that combines swimming and flying abilities."""

    def roar(self):
        """Prints roaring message."""
        print("The dragon roars!")
