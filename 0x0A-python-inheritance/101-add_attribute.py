#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(cls, key, value):
    """
    cls : the object to add an attribute to
    key : the attribute to be add
    val : the value of the add attribute

    if it is impossible to add the attribute, a typerror is raised
    """
    if not hasattr(cls, '__dict__'):
        raise TypeError("can't add attribute")
    setattr(cls, key, val)
