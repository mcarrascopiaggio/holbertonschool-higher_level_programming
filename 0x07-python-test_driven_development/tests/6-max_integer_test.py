#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """List of tests"""
    def test_ints(self):
        """test with all int in a list"""
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)
        self.assertEqual(max_integer([2, 2, 4, 4]), 4)
        self.assertEqual(max_integer([1, 265, 2, 1]), 265)
        self.assertEqual(max_integer([1, 2]), 2)

    def test_empty(self):
        """test empty list"""
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
