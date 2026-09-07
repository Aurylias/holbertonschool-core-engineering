#!/usr/bin/env python3

"""Represents a square"""


class Square:
    """Class for a square, do noting at the moment"""
    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must >= 0")
