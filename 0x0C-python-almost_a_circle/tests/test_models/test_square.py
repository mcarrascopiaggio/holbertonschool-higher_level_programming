#!/usr/bin/python3
"""Tests for Square"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """
    testing square
    """

    def test_empty(self):
        """
        test empty square
        """
        self.assertRaises(TypeError, Square, ())

    def test_error(self):
        """ 
        test error in size
        """
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(TypeError, Square, (1, 2))
        self.assertRaises(TypeError, Square, 'string')
        self.assertRaises(TypeError, Square, [1, 2, 3, 4])
        self.assertRaises(TypeError, Square, {'a': 'hola', 'b': 1})
        self.assertRaises(TypeError, Square, 1.0)

    def test_size(self):
        """ 
        test error in size
        """
        Base._Base__nb_objects = 0
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

    def test_str(self):
        """
        test string representation
        """
        s1 = Square(2, 0, 0, 45)
        self.assertEqual(s1.__str__(), "[Square] (45) 0/0 - 2")
