#!/usr/bin/python3
"""this module define a square with a private attribute (size)
the size attribute can take only pisitve integer values 
and calculates the area of a square"""


class Square:
    """the class created, the type of size attribute is checked"""

    def __init__(self, __size=0):

        """this function Instantiate with size attribute with
        positive integers"""

        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")

        self.__size = __size
    def area(self):
      
        """this method returns the area of the square"""
        return (self.__size ** 2)
