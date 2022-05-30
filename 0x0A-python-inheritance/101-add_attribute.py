#!/usr/bin/python3
"""
Write a function that adds a new attribute to an object if it’s possible
Raise a TypeError exception, with the message can't add new attribute
if the object can’t have new attribute
"""


def add_attribute(mc, name, other):
    """
    function that adds a new attribute to an object if it’s possible:
    """
    if hasattr(mc, '__dict__'):
        setattr(mc, name, other)
    else:
        raise TypeError("can't add new attribute")
