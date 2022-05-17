#!/usr/bin/python3
"""Class project"""


class Node:
    """Class Node"""
    def __init__(self, data, next_node=None):
        """Node class with two private attribute"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.data

    @setter.value:
        def data(self, value):
            self.__data = value
            if type(value) is not int:
                raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @setter.value:
        def next_node(self, value):
            self.__next_node = value
            if value is not None:
                raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    """defines a singly linked list by"""
    def __init__(self):
        """simple  instantiation"""
        self.__head = head

    def sorted_insert(self, value):
        """that inserts a new Node into the correct sorted position"""
        def sorted_insert(self, value):




