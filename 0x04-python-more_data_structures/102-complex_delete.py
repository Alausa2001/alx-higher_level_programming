#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key in new_dict.keys():
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
