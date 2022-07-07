#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for a, b in a_dictionary.items():
        if a in a_dictionary:
            a_dictionary[a] = b * 2
    return(a_dictionary)
