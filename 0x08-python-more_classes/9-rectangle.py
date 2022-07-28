#!/usr/bin/python3
"""
this module calculate the area and perimeter
of a rectangle
"""


class Rectangle:
    """defines the Rectangle the variable to
    work with is the width and height of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialze the instances with the
            varible names"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """return a printable form of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return("")
        result = ""
        if self.__height > 0 or self.__width > 0:
            for i in range(self.__height):
                result = result + (str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    result = result + "\n"
        return (result)

    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        """returns a string rep that can be evaluated
        by eval()
        """
        return("Rectangle({}, {})".format(self.width, self.height))

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

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            result = 0
            return (result)
        return (2 * (self.__height + self.__width))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """the area of two rectangles are calculated and compared"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = Rectangle.area(rect_1)
        area2 = Rectangle.area(rect_2)
        if area2 > area1:
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance"""
        return cls(size, size)
