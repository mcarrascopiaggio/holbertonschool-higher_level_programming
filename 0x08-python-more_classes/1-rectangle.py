#!/usr/bin/python3
"""
Write an empty
class Rectangle
that defines a rectangle
"""


class Rectangle:
    """
    empty class
    """
    def __init__(self, width=0, height=0):
        """init with a private attribute width & height"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """retrieve"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self)i:
        """retrieve"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
