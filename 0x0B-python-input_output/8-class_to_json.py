#!/usr/bin/python3
"""
Write a function that returns
the dictionary description with simple data structure
(list, dictionary, string, int and boolean) for JSON serialization of an obj
"""


def class_to_json(obj):
    """
    unction that returns the dictionary description
    """
    return obj.__dict__
