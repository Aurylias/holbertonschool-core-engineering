#!/usr/bin/env python3
"""Class that represente the base for geometric shapes"""


class BaseGeometry:
    """The base of geometric shapes"""

    def area(self):
        """Calculate the area of the geometric shapes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=1):
        """Check if the value is an integer or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
