#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return (ans)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
