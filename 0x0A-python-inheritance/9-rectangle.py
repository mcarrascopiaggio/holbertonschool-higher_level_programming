#!/usr/bin/python3
"""
Write an empty class BaseGeometry
third line
four line
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class BaseGeometry"""


class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
