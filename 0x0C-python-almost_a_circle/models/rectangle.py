#!/usr/bin/python3
"""module contains a class ``Rectangle`` which
inherits from class ``Base``"""


from models.base import Base


class Rectangle(Base):
    """This class inherits from ``Base`` class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """for instantiation
        for id= it calls it parent class ``Base`` for instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """sets the width of the rectctangle to a
        private class instance ``__width``"""
        self.__width = width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """assigns the height of the rectangle to a private class
        instance ``__height"""
        self.__height = height

    @property
    def x(self):
        """returns the value of x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """sets the value of x"""
        self.__x = x

    @property
    def y(self):
        """returns thevalue of y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """sets the value of y"""
        self.__y = y
