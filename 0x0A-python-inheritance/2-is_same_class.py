#!/usr/bin/python3
"""checks is an object is a ``specified`` type"""


def is_same_class(obj, a_class):
    """this function checks if ``obj`` is
    an instance of ``a_class``"""
    if type(obj) is a_class:
        return (True)
    return (False)
