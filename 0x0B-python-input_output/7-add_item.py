#!/usr/bin/python3
""" a script that adds all arguments to a Python list, and then save
them to a file:"""


import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
output_list = load(filename)
output_list = []
for i in sys.argv:
    if i != sys.argv[0]:
        output_list.append(sys.argv[1])
save(output_list, filename)
