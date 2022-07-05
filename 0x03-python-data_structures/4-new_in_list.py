#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        c = my_list.copy()
        c.pop(idx)
        c.insert(idx, element)
        return(c)
    return(my_list)
