#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle """


class Rectangle:
    """empty class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init with a private attribute width & height"""

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        return self.__width

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
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + str(self.print_symbol)
                if j == (self.__width - 1):
                    string = string + "\n"
        return string

    def __repr__(self):
        """should return a printable representation of the object"""
        return ("Rectangle({:d},{:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
