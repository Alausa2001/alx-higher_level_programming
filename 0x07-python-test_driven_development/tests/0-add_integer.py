#!/usr/bin/python3
"""this module contains a function
that adds up integers"""


def add_integer(a, b=98):
    """takes in two args(float or integer)
    if float, convert to int and returns the sum"""

    if type(a) is int or type(a) is float:
        a = int(a)
    if type(b) is int or type(b) is float:
        b = int(b)
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be an integer")
    return (a + b)
