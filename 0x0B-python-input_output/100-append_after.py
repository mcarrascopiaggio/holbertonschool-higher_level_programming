#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing aspecific str
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        f_line = f.readline()
        all_file = ""
        while f_line:
            all_file = all_file + f_line
            if search_string in f_line:
                all_file = all_file + new_string
            f_line = f.readline()
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(all_file)
