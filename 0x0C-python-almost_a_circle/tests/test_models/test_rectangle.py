#!/usr/bin/python3
"""Tests for Rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
   """
   Rectangle test
   """

   def test_class(self):
        self.assertRaises(TypeError, Rectangle, ())

    if __name__ == "__main__":
        unittest.main()
