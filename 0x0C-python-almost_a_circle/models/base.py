#!/usr/bin/python3
"""this module contians the base class ``Base()`` the class has
a private class attribute ``__nb_objects``
This class will be the “base” of all other classes in this project
. The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file:
        list_objs is a list of instances who inherits of Base - example: list
        of
        Rectangle or list of Square instances"""
        filename = cls.__name__ + ".json"
        list_dict_instances = [i.to_dictionary() for i in list_objs]
        empty = []
        if list_objs is None:
            with open(filename, 'w') as filename:
                filename.write(cls.to_json_string(empty))
        elif list_objs is not None:
            with open(filename, 'w') as filename:
                filename.write(cls.to_json_string(list_dict_instances))
