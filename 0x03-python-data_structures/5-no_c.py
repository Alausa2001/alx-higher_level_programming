#!/usr/bin/python3
def no_c(my_string):
    for a in range(len(my_string)):
        if my_string[a]  != 'c':
            if my_string[a]  != 'C':
                print(my_string[a], end='')
    return('')

