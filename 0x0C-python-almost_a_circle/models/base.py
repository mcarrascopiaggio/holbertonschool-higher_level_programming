#!/usr/bin/python3
"""
Write the first class Base
"""


import json
import os


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
                    my_List.append(cls.to_dictionary(item))
                return myFile.write(cls.to_json_string(my_List))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        my_List = []
        if json_string is None:
            return my_List
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        arg **dictionary can be thought of as a double pointer to a dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
