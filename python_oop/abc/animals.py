#!/usr/bin/env python3
"""Module containing class for animals"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals"""

    @abstractmethod
    def sound(self):
        """Emit a sound"""


class Dog(Animal):
    """Represent a dog"""

    def sound(self):
        """Make the dog bark"""
        return "Bark"


class Cat(Animal):
    """Represent a cat"""

    def sound(self):
        """Make the cat meow"""
        return "Meow"
