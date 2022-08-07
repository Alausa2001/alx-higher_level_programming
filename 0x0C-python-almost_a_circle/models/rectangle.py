class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property    
    def width_getter(self):
        return (self.__width)
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        return (self.__height)
    
    @height.setter
    def height(self, height):
        self.__height = height
        
    @property
    def x_getter(self):
        return (self.__x)
    
    @x_setter.setter
    def x_setter(self, x):
        self.__x = x
        
    @property
    def y_getter(self):
        return (self.__y)
    
    @y_setter.setter
    def y_setter(self, y):
        self.__y = y
