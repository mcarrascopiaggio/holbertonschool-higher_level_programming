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

    @property
    def size(self):
        """ retrieve itself"""
        return self.__size

    @size.setter
    def size(self, size):
        """ property setter """
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """function that eturns the current square area"""
        return self.__size * self.__size

    def __lt__(self, other):
        """describes less than operator(<)"""
        return ((self.area) < (other.area))

    def __le__(self, other):
        """descries less than or equal to (<=)"""
        return ((self.area) <= (other.area))

    def __gt__(self, other):
        """describes greater than (>)"""
        return ((self.area) > (other.area))

    def __ge__(self, other):
        """describes greater than or equal to (>=)"""
        return ((self.area) >= (other.area))

    def __eq__(self, other):
        """describes equality operator(==)"""
        return ((self.area) == (self.other))

    def __ne__(self, other):
        """describes not equal to operator(!=)"""
        return ((self.area) != (self.other))
