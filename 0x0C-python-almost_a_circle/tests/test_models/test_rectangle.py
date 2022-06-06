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

    def test_documentation(self):
        """
        documentation test
        """
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.width.__doc__) > 0)
        self.assertTrue(len(Rectangle.height.__doc__) > 0)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_rectangle(self):
        """
        test some rectangle
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_height_error(self):
        """
        height error test
        """
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 10, -1)
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, -1, 10)
        self.assertRaises(TypeError, Rectangle, 10, (2, 1))
        self.assertRaises(TypeError, Rectangle, 10, 'string')
        self.assertRaises(TypeError, Rectangle, 10, [1, 2, 3])
        self.assertRaises(TypeError, Rectangle, 10, {'a': 1, 'b': 2})
        self.assertRaises(TypeError, Rectangle, 10, 1.0)
        self.assertRaises(TypeError, Rectangle, 1.0, 2.5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5)

    def test_width(self):
        """ width test """
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, -1, 10)
        self.assertRaises(TypeError, Rectangle, (1, 2), 10)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -10)
        self.assertRaises(TypeError, Rectangle, 'string', 10)
        self.assertRaises(TypeError, Rectangle, [1, 2, 3], 10)
        self.assertRaises(TypeError, Rectangle, {'a': 1, 'b': 2}, 10)
        self.assertRaises(TypeError, Rectangle, 1.5, 10)
        self.assertRaises(TypeError, Rectangle, 2.5, 10)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5)

    if __name__ == "__main__":
        unittest.main()
