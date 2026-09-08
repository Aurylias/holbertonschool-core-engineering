#!/usr/bin/env python3
"""A module that handle the base for geometric shapes"""


class BaseGeometry:
    """Class that represente the base for geometric shapes"""

    def area(self):
        """Calculate the area of the geometric shapes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=1):
        """Check if the value is an integer or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True

class Rectangle(BaseGeometry):
    """Class that represente a square"""
    def __init__(self, width=1, height=1):
        """Constructor"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
