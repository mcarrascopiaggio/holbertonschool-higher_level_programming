#!/usr/bin/python3
"""
Write an empty class BaseGeometry
third line
four line
"""

Rectangle = __import__('9-rectangle').Rectangle
"""import class Rectangle"""


class Square(Rectangle):
    """
    Write a class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """
        [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
