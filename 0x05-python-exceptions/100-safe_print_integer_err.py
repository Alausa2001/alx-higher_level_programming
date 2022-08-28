#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return(True)
    except ValueError as error:
        # stderr.write(error)
        print("Exception: {}".format(error), file=stderr)
        return False
