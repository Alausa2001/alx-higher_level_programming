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
    
    @classmethod
    def test_class_setup(cls):
        """test square instance creation"""
        Base._Base__nb_objects = 0
        sqr = Square(1, 2, 3, 4)
        sqr2 = Square(1, 2, 3)
    def test_arg_values(self):
        sqr = Square(1, 2, 3, 4)
        sqr2 = Square(1, 2, 3)

        self.assertEqual(sqr.size, 1)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)
        self.assertEqual(sqr.id, 4)
        self.assertEqual(sqr2.id, 5)

