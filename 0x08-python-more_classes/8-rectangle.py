#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    """Define class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """that returns the rectangle perimeter"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """should print the rectangle with the character #:"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + str(self.print_symbol)
                if i < (self.__height - 1):
                    string = string + "\n"
            return string

    def __repr__(self):
        """ should return a string rep of rectangle to recreate a new in()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
