#!/usr/bin/python3
"""Printing a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """init with a private attribute size"""

        self.__size = size
        self.__position = position

    def area(self):
        """Return the area of a square"""

        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.position(0) < 0 or self.position(1) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Printing a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("-", end="")
                print()
