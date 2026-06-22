#!/usr/bin/env python3
"""Module that defines Animal abstract class with Dog and Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """A class that defines a Dog."""

    def sound(self):
        """Returns the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A class that defines a Cat."""

    def sound(self):
        """Returns the sound a cat makes."""
        return "Meow"
