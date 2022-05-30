#!/usr/bin/python3
"""
Write an empty class BaseGeometry
third line
four line
"""


class BaseGeometry():
    """
    empty class
    """

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
