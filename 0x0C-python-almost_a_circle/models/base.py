#!/usr/bin/python3
"""
Write the first class Base
"""


import json


class Base():
    """
    Create a file named
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor: def __init__(self, id=None)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        my_List = []
        with open(filename, mode='a', encoding="utf-8") as myFile:
            if list_objs is None:
                return myFile.write("")
            else:
                for items in list_objs:
                    my_List.append(items.to_dictionary())
                return myFile.write(cls.to_json_string(my_List))
