#!/usr/bin/python3
"""contains a class that has method ``area``"""


class BaseGeometry:
    """has two methods (area() and integer_validator()"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if the value of name is an integer
        if True then check if the value is greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a subclass of BaseGeometry"""

    def __init__(self, width, height):
        """validates the value of width and height
        before intiallization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
