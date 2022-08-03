#!/usr/bin/python3
"""moudle con ains function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """returns the dict rep of obj"""
    return obj.__dict__
