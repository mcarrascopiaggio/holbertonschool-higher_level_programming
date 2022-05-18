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
        self.__width = width

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
        self.__height = height

    @height.setter
    def height(self, value):
        """conditions"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")