#!/usr/bin/python3
"""
This module contains function that prints My name is.
first_name and last_name must be strings
or raise a TypeError exception
"""


def say_my_name(first_name, last_name=""):
    """
    First line
    Second Line
    Third Line
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
