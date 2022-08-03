#!/usr/bin/python3
"""contains a class that has method ``area``"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
