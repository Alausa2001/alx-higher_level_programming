#!usr/bin/python3
"""Module contains unittest for
``max_integer``"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TESTMAXINTEGER(unittest.TestCase):
    """unittest class for max_integer"""

    def test_max(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([1, 2, 3, 2, 1]), 3)
        self.assertAlmostEqual(max_integer([-2, -3]), -2)
        self.assertAlmostEqual(max_integer([7, 3, 3]), 7)
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
