#!/usr/bin/python3
"""
Save Object to a file
Write a function that writes an Object to a text file,
using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file
    """
    with open(filename, mode='w', encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(my_obj))
