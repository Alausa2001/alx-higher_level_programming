#!/usr/bin/python3
"""accounting for blankline"""
def example(b=[]):
    """
    >>> c = [1, 22, 3, 55, 6, 90]
    >>> example(c)
    1
    <BLANKLINE>
    22
    <BLANKLINE>
    3
    <BLANKLINE>
    55
    <BLANKLINE>
    6
    <BLANKLINE>
    90
    <BLANKLINE>
    """
    for i in b:
        print(i)
        print()
def whitespace(b=[]):
    for i in range(len(b)):
        if i < len(b) - 1:
            print(b[i], end=', ')
    print(b[len(b) - 1], end='')
    """only matching whitespace passes the test and the whitespace character
    doesn't matter
    >>> c = [1, 2, 3, 4] #doctest: +NORMALIZE_WHITESPACE
    >>> whitespace(c) #doctest: +NORMALIZE_WHITESPACE
    1, 2, 
    3,                                                       4  
    """
