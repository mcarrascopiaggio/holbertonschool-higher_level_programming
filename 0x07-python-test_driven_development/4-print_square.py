#!/usr/bin/python3
"""
function that prints a square with the character #
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception
f size is less than 0, raise a ValueError
if size is a float and is less than 0, raise a TypeError
"""


def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    line = "#" * size
    for i in range(size):
        print(line)

