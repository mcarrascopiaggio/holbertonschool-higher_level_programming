#!/usr/bin/python3
"""
Write a class MyInt that inherits from int
third line
fourth line
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """
        change return to
        False"""
        return False

    def __ne__(self, other):
        """
        change return to True
        """
        return True
