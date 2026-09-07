#!/usr/bin/env python3

"""Module handling a square"""


class Square:
    """Class for a square, do noting at the moment"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with a given size"""
        if not isinstance(size, int) or not isinstance(position, tuple):
            raise TypeError("size must be an integer")
        elif size < 0 or (len(position) < 2 and (position[0 < 1 or 
                          position[1 < 1]])):
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def __str__(self):
        """Handle how square is printed"""
        self.my_print()
        return ""

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("size must be an integer")
        elif len(value) < 2:
            raise ValueError("size must be >= 0")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for k in range(self.__position[0] - 1):
                        print(" ", end="")
                for j in range(self.size):
                    if j == (self.size - 1):
                        print("#")
                    else:
                        print("#", end="")

square = Square(3, (4, 1))
square.my_print()
print(square)
