#!/usr/bin/python3
"""Class project - Square"""


class Square:
    """empty class Square with a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """function init Square class with two private attribute size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ retrievit itself"""
        return self.__position

    @position.setter
    def position(safe, value):
        """propertt setter"""
        self.__position = value
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """function that eturns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                for o in range(self.position[0]):
                    print(" ", end="")
                for m in range(self.size):
                    print("#", end="")
                print()
