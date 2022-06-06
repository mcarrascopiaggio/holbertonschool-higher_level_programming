#!/usr/bin/python3
"""Tests for Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """
    Base test
    """

    def test_default_id(self):
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
