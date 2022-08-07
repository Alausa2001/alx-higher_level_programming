#!/usr/bin/python3
"""this module contians the base class ``Base()`` the class has
a private class attribute ``__nb_objects``
This class will be the “base” of all other classes in this project
. The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)"""


class Base:
    """this class  has an ``__init__() `` constructor for instantiation of the
    instances and a private attribute ``__nb__objects``"""

    __nb_objects = 0

    def __init__(self, id=None):
        """it instantites the instances."""
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = self.__nb_objects
