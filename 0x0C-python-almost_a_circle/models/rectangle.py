#!/usr/bin/python3
"""
2. First Rectangle
Write the class Rectangle that inherits from Base
"""


from models.base import Base
import sys


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.
            Args:
                width and height: int, sides of rectangle
                x and y: has no function yet
                id: id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
            Arg:
                value: must be int >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height, value mus be > 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x, value must be >= 0"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y, value must be >= 0"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
         that returns the area value of
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"""

    def display(self):
        """
        to print in stdout the Rectangle instance with
        the character # by taking care of x and y
        """
        for lines in range(self.__y):
            print()
        for row in range(self.__height):
            for spaces in range(self.__x):
                print(" ", end="")
            for colum in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes
        """
        list_args = ['id', 'width', 'height', 'x', 'y']
        if args:
            if len(args) < 6:
                for i in range(len(args)):
                    setattr(self, list_args[i], args[i])
        else:
            if kwargs:
                for key in kwargs:
                    if key in list_args:
                        setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dic = {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
                }
        return dic
