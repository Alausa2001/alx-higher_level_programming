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
        with self.assertRaises(TypeError):
            Square(1, '2')
        with self.assertRaises(TypeError):
            Square(1, 2, '3')
        with self.assertRaises(TypeError):
            Square(1, 2, '3', 4)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)


    def test_str_Square(self):
        sqr = Square(1, 2, 3, 4)
        ans = '[Square] (4) 2/3 - 1'
        self.assertEqual(sqr.__str__(), ans)
    
    def test_to_dictionaary(self):
        sqr = Square(1, 2, 3, 4)
        ans = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(sqr.to_dictionary(), ans)


    def test_update(self):
        sqr = Square(1)
        sqr.update(2, 3, 4, 9)
        self.assertEqual(sqr.__str__(), '[Square] (2) 4/9 - 3')
        sqr2 = Square(2)
        sqr2.update(id=2, size=3, x=4, y=9)
        self.assertEqual(sqr2.__str__(), '[Square] (2) 4/9 - 3')
        
        sqr = Square(2, 0, 0, 2)
        self.assertEqual(str(sqr), "[Square] (2) 0/0 - 2")
        sqr.update(size=10)
        self.assertEqual(str(sqr), "[Square] (2) 0/0 - 10")
        sqr.update(size=11, x=2)
        self.assertEqual(str(sqr), "[Square] (2) 2/0 - 11")
        sqr.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(sqr), "[Square] (89) 5/3 - 4")


    def test_create(self):
        sqr = Square(1, 2, 3, 4)
        ans_dict = sqr.to_dictionary()
        ans = Square.create(**ans_dict)
        self.assertEqual('[Square] (4) 2/3 - 1', str(ans))

















