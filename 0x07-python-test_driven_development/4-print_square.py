#!/usr/bin/python3
"""
function that prints a square with the character #
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception
"""


def print_square(size):
    """
    function prints a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
