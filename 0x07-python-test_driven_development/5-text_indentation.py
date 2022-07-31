#!/usr/bin/python3
""" function that prints a text with 2 new lines after each of
these characters: ., ? and :"""


def text_indentation(text):
    """a string is taken as argument and
    the string with blank lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    test = ""
    for a in text:
        test += a
        if a in ".?:":
            test = test.strip()
            test += '\n'
            print(test)
            test = ""
    print(test.strip(), end='')
