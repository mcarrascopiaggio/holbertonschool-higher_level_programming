#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns the string format for print
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"

    @property
    def size(self):
        """
        retrievit
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets width & height with size
        """
        self.width = size
        self.height = size
