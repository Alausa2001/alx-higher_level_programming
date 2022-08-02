#!/usr/bin/python3
"""Module checks if objects are of same instance
or inherited (direclty of indiresctly)"""


def inherits_from(obj, a_class):
    """Check if args are of same instance directly or indirectly"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    return (False)
