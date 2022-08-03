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

    def to_json(self):
        """return a dict rep of the Student"""
        return (self.__dict__)
