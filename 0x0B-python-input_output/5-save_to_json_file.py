#!/usr/bin/python3
"""module contains a  function that writes an Object
to a text file, using a JSON representation:"""


import json


def save_to_json_file(my_obj, filename):
    """args: my_obj= object to be writtrn into the file
    filename= file to write my_obj to"""
    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
