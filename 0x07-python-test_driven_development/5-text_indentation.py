#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :
text must be a string, otherwise raise a TypeError
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i == "?" or i == ":":
            print()
            print()
        else:
            print(i, end="")
