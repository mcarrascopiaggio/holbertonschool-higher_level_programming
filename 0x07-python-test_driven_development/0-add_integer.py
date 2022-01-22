#!/usr/bin/python3
"""
follow tge add function
return: a sum of two arguments
raise an error if a or b are not int or float
"""


def add_integer(a, b=98):

    """
    function that adds 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
