#!/usr/bin/python3
"""the function in this module prints a square"""


def print_square(size):
    """print_square() takes in an argument of type int
    and print a square
    """
    c = ""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size >= 0:
        for i in range(size):
            c += '#' * size
            if i != size - 1:
                c += '\n'
        print(c)
