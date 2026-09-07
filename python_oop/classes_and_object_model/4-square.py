#!/usr/bin/env python3

"""Represents a square"""


class Square:
    """Class for a square, do noting at the moment"""
    def __init__(self, size=0):
        """Instantiation with a given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    @property
    def __size(self):
        """Give access to the value of __size"""
        return self.__size
    
    @__size.setter
    def __size(self, value):
        """Set the __size to the given value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
