#!/usr/bin/python3
"""Tests for Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class test_Base(unittest.TestCase):
    """
    Base test
    """

    def test_default_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_entry_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)
        b6 = Base(0)
        self.assertEqual(b6.id, 0)
        b7 = Base(-1)
        self.assertEqual(b7.id, -1)

    def test_documentation(self):
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_create_rec(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertDictEqual(r1_dictionary, r2.to_dictionary())

    def test_create_sq(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertDictEqual(s1_dictionary, s2.to_dictionary())

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_from_json_string_s(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)

    if __name__ == '__main__':
        unittest.main()
