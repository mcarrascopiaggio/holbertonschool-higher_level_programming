#!/usr/bin/python3
"""
Write a class Student that defines a student by
public instances & public method
"""


class Student():
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that writes an Object to a text file, using a JSON rep:
        """
        aux = {}
        if type(attrs) == list:
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
                if key in self.__dict__:
                    aux[key] = self.__dict__[key]
            return aux
        else:
            return self.__dict__
