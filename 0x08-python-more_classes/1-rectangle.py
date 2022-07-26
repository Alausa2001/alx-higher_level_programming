#!/usr/bin/python3
"""
this module assigns value to the
variables of a rctangle
"""


class Rectangle:
    """defines the Rectangle the variable to
    work with is the width and height of a rectangle"""

    def __init__(self, width=0, height=0):
        """initialze the instances with the
            varible names"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return the width value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """heigth getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
