#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file
    and print it in the stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
