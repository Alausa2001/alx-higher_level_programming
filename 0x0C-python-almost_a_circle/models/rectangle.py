#!/usr/bin/python3
"""module contains a class ``Rectangle`` which
inherits from class ``Base``"""


from base import Base


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
    def width(self, value):
        """sets the width of the rectctangle to a
        private class instance ``__width``"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """assigns the height of the rectangle to a private class
        instance ``__height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns thevalue of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """displays the rectangle using ``#``"""
        result = ""
        if self.__y > 0:
            print('\n' * self.__y, end='')
        for i in range(self.__height):
            if self.__x > 0:
                result += ' ' * self.__x
            result += '#' * self.__width
            if i < self.__height - 1:
                result += '\n'
        print(result)
        return(result)

    def __str__(self):
        """print the ???"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                self.x,
                                                                self.y,
                                                                self.width,
                                                                self.height)

    def update(self, *args, **kwargs):
        """ public method def update(self, *args): that assigns
        an argument to each attribute:"""
        if args:
            for count, arg in enumerate(args, 1):
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.__width = arg
                elif count == 3:
                    self.__height = arg
                elif count == 4:
                    self.__x = arg
                elif count == 5:
                    self.__y = arg
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """return the dict representaion of class ``Rectangle``"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
