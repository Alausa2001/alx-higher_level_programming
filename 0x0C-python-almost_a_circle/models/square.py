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
    def update(self, *args, **kwargs):
        """ that assigns attributes"""
        if args:
            for count, arg in enumerate(args, 1):
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.size = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwarg['y']
