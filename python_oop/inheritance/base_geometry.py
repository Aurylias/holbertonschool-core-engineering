#!/usr/bin/env python3
"""Class that represente the base for geometric shapes"""


class BaseGeometry:
    """The base of geometric shapes"""
    def __init__(self, sides=0, width=0, height=0):
        """Constructor"""
        if self.integer_validator("sides", sides):
            self.__sides = sides
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """Calculate the area of the geometric shapes"""
        return self.__width * self.__height

    def integer_validator(self, name="", value=1):
        """Check if the value is an integer or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")
        return True
