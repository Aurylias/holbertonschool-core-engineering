#!/usr/bin/env python3
"""A module that handle the base for geometric shapes"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class that represent a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area():
        """Calculate the area of the square"""
        return self.__size * self.__size
