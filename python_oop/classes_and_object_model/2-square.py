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
