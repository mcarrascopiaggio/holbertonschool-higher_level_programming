#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle """


class Rectangle:
    """empty class"""
    def __init__(self, width=0, height=0):
        """init with a private attribute width & height"""

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the rectangle perimeter
        if width or height is equal to 0, perimeter is equal to 0
        """
        perimeter = (self.__height * 2) + (self.__width * 2)
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """return a sring representation"""
        string = ""
        if 0 in [self.__width, self.__height]:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + "#"
                if i != self.__height - 1:
                    string = string + "\n"
        return string
