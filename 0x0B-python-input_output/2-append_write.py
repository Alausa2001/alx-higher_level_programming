#!/usr/bin/python3
"""contains a function that appends a
text into a file"""


def append_write(filename="", text=""):
    """args: filename= file to be written into
    text= what to write into the file"""
    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
