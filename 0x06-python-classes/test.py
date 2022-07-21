class Square:
    """the class created, the type of size attribute is checked"""

    def __init__(self, __size=0):

        """this function Instantiate with size attribute with
        positive integers"""
        self.size = size
    @property
    def size(self):
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    def area(self):

        """this method returns the area of the square"""

        return (self.__size ** 2)
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)