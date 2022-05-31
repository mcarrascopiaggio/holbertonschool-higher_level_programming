#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file:"""
from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    my_list = load_from_json_file('add_item.json')
    save_to_json_file(my_list + argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
