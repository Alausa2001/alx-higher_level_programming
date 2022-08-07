#!/usr/bin/python3
"""contains test for Base class"""


import unittest
from models.base import Base


class TESTBASE(unittest.TestCase):
    """Base class test"""

    
    def test_attr_present(self):
        """test if Base has an attribute ``__nb_objects"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_id(self):
        """test for if id is None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id2(self):
        """if id is none"""
        b2 = Base()
        self.assertEqual(b2.id, 2)
    
    def test_id_value(self):
        """if id is given a value"""
        b1 = Base(99)
        self.assertEqual(b1.id, 99)
    
    def test_instance_multiple_args(self):
        """if excess agrs are given on instatiation"""
        with self.assertRaises(TypeError):
            b3 = Base(12, 23)







if __name__ == "__main__":
        unittest.main()
