#!/usr/bin/python3
"""function that returns the JSON representation of an object
(string)"""


import json as js


def to_json_string(my_obj):
    """returns the json rep of a string"""
    return (js.dumps(my_obj))
