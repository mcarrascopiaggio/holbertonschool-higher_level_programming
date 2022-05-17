#!/usr/bin/python3
"""Class project - Square"""


class Square:
    """empty class Square with a private attribute"""
    def __init__(self, size=0):
        """function init Square class with a private attribute size"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size <0:
            raise ValueError("size must be >= 0")
