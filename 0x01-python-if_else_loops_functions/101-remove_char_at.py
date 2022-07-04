#!/usr/bin/python3
def remove_char_at(str, n):
    for a in range(0, len(str)):
        if a != n:
            print((str[a]), end='')
    return('')
