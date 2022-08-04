#!/usr/bin/python3
"""This module contains a class ``Student``"""


class Student:
    """this class has two method (the init method =
    instantiation and to_json method that retrieves a dictionary representation
    of a student"""

    def __init__(self, first_name, last_name, age):
        """instatiates the instances with a first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dict rep of the Student
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved"""
        new = {}
        me = (self.__dict__)
        if type(attrs) is list:
            for i in attrs:
                for key, j in me.items():
                    if i == key:
                        new[key] = j
            return (new)
        return (me)

    def reload_from_json(self, json):
        """Public method def reload_from_json(self, json): that replaces all
        attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        You are not allowed to import any module"""
        for key, value in json.items():
            setattr(self, key, value)
