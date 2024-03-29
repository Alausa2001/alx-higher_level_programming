#!/usr/bin/python3
"""this module contians the base class ``Base()`` the class has
a private class attribute ``__nb_objects``
This class will be the “base” of all other classes in this project
. The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)"""


import json
import csv


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
        list_dict_instances = []

        if list_objs is not None:
            list_dict_instances = [i.to_dictionary() for i in list_objs]
        with open(filename, 'w') as filename:
            filename.write(cls.to_json_string(list_dict_instances))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        json_string is a string representing a list of dictionaries"""
        if json_string is None or not json_string:
            empty = '[]'
            return json.loads(empty)
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set:"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as filename:
                read_json_string = filename.read()
                python_string = cls.from_json_string(read_json_string)
                return [cls.create(**i) for i in python_string]
        except (FileNotFoundError, IOError):
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save list of insatnce to csv file"""
        filename = cls.__name__ + ".csv"
        fieldnames_re = ['id', 'width', 'height', 'x', 'y']
        fieldname_s = ['id', 'size', 'x', 'y']
        with open(filename, 'w') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    writer = csv.DictWriter(filename, fieldnames=fieldnames_re)
                else:
                    writer = csv.DictWriter(filename, fieldnames=fieldnames_s)
                for obj in list_obj:
                    writer.Writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads object from csv file"""
        filename = cls.__name__ + '.csv'
        empty = []
        try:
            with open(filename, 'r') as csvfile:
                content = csv.DictReader(csvfile)
                for args in content:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                        obj = cls.create(**dictionary)
                    empty.append(obj)
        except (FileNotFoundError, IOError):
            return []
