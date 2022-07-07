#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for a, b in sorted(a_dictionary.items()):
        print("{}: {}".format(a, b))
    return('')
