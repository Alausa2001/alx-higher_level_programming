import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUp(cls):
        Base._Base__nb_objects = 0
        cls.rect1 = Rectangle(5, 10)
        cls.rect2 = Rectangle(2, 4, 6)
        cls.rect3 = Rectangle(3, 6, 9, 12)
        cls.rect4 = Rectangle(2, 4, 6, 8, 10)

    def test_id_class(self):
        """test for id access through a classmethod"""
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect4.id, 10)
        self.assertEqual(self.rect2.id, 2)


    def test_class(self):
        '''
        Rectangle is a class
        '''
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''
        Tests if Rectangle inherits Base.
        '''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_4(self):
        
        """test for if id is access through the base class"""
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        b4 = Base(69)
        b5 = Base(4)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 69)
        self.assertEqual(b5.id, 4)

    def test_id(self):
        """test if id is accessed through Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
    
    def test_Exceptions(self):
        """tests for raised exceptions"""

        with self.assertRaises(TypeError):
            r = Rectangle("1", 2) 

        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)
    def test_area(self):
        """tests for the area of the rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
    def test_display(self):
        """tests for display() method"""
        result = '##\n##'
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.display(), result)
    def test_str(self):
        """ test for ???"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        result = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(r1.__str__(), result)

