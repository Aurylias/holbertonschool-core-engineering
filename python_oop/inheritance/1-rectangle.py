#!/usr/bin/env python3
"""A module that handle the base for geometric shapes"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represente a square"""
    def __init__(self, width=1, height=1):
        """Constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
