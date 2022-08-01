#!/usr/bin/python3
"""the function in This module returns a list of all
the available attributes and methods of an object"""


def lookup(obj):
    """takes object ``obj`` as an argument
    and returns a list of all the attributes and methods
    of the object"""
    return (dir(obj))
