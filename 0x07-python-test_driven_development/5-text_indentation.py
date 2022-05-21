#!/urs/bin/python3
"""
 function that prints a text with 2 new lines after each of these characters
 text must be a string
 raise a TypeError
 """


def text_indentation(text):
    """
    prints a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for i in range(len(text)):
        print(text[i], end='')
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print('\n')
        if i < (len(text) - 1):
            if text[i + 1] == ' ':
                i += 1
        while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
            i += 1
