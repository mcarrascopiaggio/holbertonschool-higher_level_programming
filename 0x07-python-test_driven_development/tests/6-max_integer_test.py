#!/usr/bin/python3
"""
unittest 6
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test function Max Integer"""

    def test_succes_int(self):
        """test max of integers"""
        self.assertEqual(max_integer([1, 2, 3, 8]), 8)

    def test_succes_int_end(self):
        """test max of int changing order"""
        self.assertEqual(max_integer([8, 2, 3, 1]), 8)

    def test_succes_float(self):
        """test max of float"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 8.0]), 8.0)

    def test_succes_float_end(self):
        """test max of floats"""
        self.assertEqual(max_integer([8.0, 2.0, 3.0, 1.0]), 8.0)

    def test_succes_mix(self):
        """test max of mix int and floats"""
        self.assertEqual(max_integer([8.0, 2, 3, 1.0]), 8.0)

    def test_succes_mix2(self):
        """test max of mix int and floats II"""
        self.assertEqual(max_integer([8, 2, 3, 1.0]), 8)

    def test_succes_negatives(self):
        """test negatives"""
        self.assertEqual(max_integer([-1, -3]), -1)

    def test_succes_oneE(self):
        """test with only one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_succes_empty(self):
        """test the null condition"""
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
