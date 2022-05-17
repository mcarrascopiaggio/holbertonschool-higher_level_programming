#!/usr/bin/python3
"""Class project - Square"""


class Square:
    """empty class Square with a private attribute"""
    def __init__(self, size=0):
        """function init Square class with a private attribute size"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ retrieve itself"""
        return self.__size

    @size.setter
    def size(self, size):
        """ property setter """
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """function that eturns the current square area"""
        return self.__size * self.__size
