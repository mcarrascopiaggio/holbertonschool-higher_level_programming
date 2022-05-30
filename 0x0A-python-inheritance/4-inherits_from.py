#!/usr/bin/python3
"""
Write a function that returns True
if the object is an instance of a class that inherited
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    """
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False
