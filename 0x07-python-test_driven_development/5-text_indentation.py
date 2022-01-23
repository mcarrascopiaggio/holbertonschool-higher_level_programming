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
    text = text.strip()
    last_c = len(text) -1
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] == '.' or text[c] == '?' or text [c] == ':':
            print()
            print()
            if c == last_c:
                break
            if text[c + 1] == ' ':
                c = c + 1
        c = c + 1
