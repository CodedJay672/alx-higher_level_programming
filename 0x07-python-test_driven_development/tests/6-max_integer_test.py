#!/usr/bin/python3
"""
Unittest for max_integer([..])

"""
import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test cases"""
    def test_emptyArgs(self):
        self.assertIsNone(max_integer(), None)

    def test_oneArg(self):
        self.assertEqual(max_integer([4]), 4)

    def test_maxLast(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxFirst(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_emptyList(self):
        self.assertIsNone(max_integer([]), None)
