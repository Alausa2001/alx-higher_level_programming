#!/usr/bin/python3
"""test for the class Square(a subclass a Rectangle which is a
subclass of Base)"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""
    
    def test_arg_values(self):
        sqr = Square(1)
        sqr2 = Square(1, 2)
        sqr3 = Square(1, 2, 3)
        sqr4 = Square(1, 2, 3, 4)

        self.assertEqual(sqr.size, 1)
        self.assertEqual(sqr2.x, 2)
        self.assertEqual(sqr3.y, 3)
        self.assertEqual(sqr4.id, 4)
        self.assertEqual(sqr2.id, 6)
    

    def test_wrong_vals(self):
        """this module test if the correct type or value is given to an argument"""

        with self.assertRaises(TypeError):
            Square('1')

