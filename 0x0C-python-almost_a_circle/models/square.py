#!/usr/bin/python3
"""module contains a class `Square` that inherits for Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """the class; it is a subclass of Rectangle which is a subclass of Base"""

    def __init__(self, size, x=0, y=0, id=None):
        """it initialize the args of the instances upon creation"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return the parameters of the square"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                          self.y, self.size))

    @property
    def size(self):
        """size getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
