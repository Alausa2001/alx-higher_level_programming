#!/usr/bin/python3
"""checks if an object is an instance of
the class specified or the superclass of the
class specified"""


def is_kind_of_class(obj, a_class):
    """checks if ``obj`` is an instance of ``class``"""
    return (isinstance(obj, a_class))
