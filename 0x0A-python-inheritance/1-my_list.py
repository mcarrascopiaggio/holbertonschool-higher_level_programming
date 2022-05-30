#!/usr/bin/python3
"""
1-my_list.py
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    pass

    def print_sorted(self):
        """
        that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
