#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Define class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieve it"""
        return self.__width = width

    @width.setter
    def width(self, value):
        """condition"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ retrieve it"""
        return self.__height = height

    @height.setter
    def height(self, value):
        """conditions"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """that returns the rectangle perimeter"""
        return (self.__width * 2) + (self.__height * 2)
