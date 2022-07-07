#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if type(my_list) is list:
        c = my_list.copy()
        for i in range(len(c)):
            if c[i] == search and c[i]:
                c[i] = replace
    return(c)
