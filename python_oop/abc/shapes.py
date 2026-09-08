#!/usr/bin/env python3
"""Module that handle shapes"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """A class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""


class Circle(Shape):
    """Class handling circles"""
    
    def __init__(self, radius):
        """Constructor"""
        if not isinstance(radius, int):
            raise TypeError("radius must be an interger")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return pi * (self.__radius * self.__radius)

    def perimeter(self):
        """Calculate the perimeter of the circle"""
        return 2 * pi * self.__radius

class Rectangle(Shape):
    """Class handling rectangle"""

    def __init__(self, width, height):
        """Constructor"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Function to give shape info"""
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
