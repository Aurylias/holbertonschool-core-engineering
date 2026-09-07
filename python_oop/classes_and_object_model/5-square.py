#!/usr/bin/env python3

"""Module handling a square"""


class Square:
    """Class for a square, do noting at the moment"""
    def __init__(self, size=0):
        """Instantiation with a given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Give access to the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the __size to the given value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range (self.size):
                    if j == (self.size - 1):
                        print("#")
                    else:
                        print("#", end="")

square = Square(5)
square.my_print()
