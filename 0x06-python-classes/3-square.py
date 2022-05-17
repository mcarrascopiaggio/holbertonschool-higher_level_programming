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

    def area(self):
        """function that eturns the current square area"""
        return self.__size * self.__size
