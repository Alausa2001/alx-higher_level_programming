#!/usr/bin/python3
"""module contains a fnction tha writes into a file"""


def write_file(filename="", text=""):
    """``write_file()``takes two args(file to be wriiten into
    and the text to write into the file) then returns the number of
    chars written into the file"""
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
