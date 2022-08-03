#!/usr/bin/python3
"""module contains a unction that creates an Object
from a “JSON file”:"""


import json as js


def load_from_json_file(filename):
    """ ``load_from_json_file() craetes an object
    from json file
    args: filename=json file from which the object is
    created"""
    with open(filename, 'r', encoding='utf-8') as my_file:
        js.load(my_file)
