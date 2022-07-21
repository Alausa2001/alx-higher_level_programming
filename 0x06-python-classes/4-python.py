#!/usr/bin/python3
"""this module define a square with a private attribute (size)
the size attribute can take only pisitve integer values
and calculates the area of a square"""


class Square:
    """the class created, the type of size attribute is checked"""

    def __init__(self, size=0):

        """this function Instantiate with size attribute with
        positive integers"""
        self.size = size
        
    @property
    def size(self):
        
        """ value getter"""
        
        return (self.__size)
    
    @size.setter
    def size(self, value):
        
        """value setter"""
        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    def area(self):

        """this method returns the area of the square"""

        return (self.__size ** 2)
