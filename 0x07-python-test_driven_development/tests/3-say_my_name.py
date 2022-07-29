#!/usr/bin/python3
""" This module print the name of a person"""


def say_my_name(first_name, last_name=""):
    """Takes two args of type(str)"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {}". format(first_name), end=' ')
    print("{}".format(last_name))
