#!/usr/bin/env python3

"""Represents a square"""


class Square:
    """Class for a square, do noting at the moment"""
    def __init__(self, size):
        if size.is_integer():
            self.__size = size
        elif not size.is_integer():
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
