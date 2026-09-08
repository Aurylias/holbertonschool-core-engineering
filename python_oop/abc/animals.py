#!/usr/bin/env python3
"""Module containing class for animals"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals"""

    @abstractmethod
    def sound():
        """Emit a sound"""


class Dog(Animal):
    """Represent a dog"""

    def sound():
        """Make the dog bark"""
        return "Bark"


class Cat(Animal):
    """Represent a cat"""

    def sound():
        """Make the cat meow"""
        return "Meow"
