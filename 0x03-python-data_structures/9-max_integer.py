#!/usr/bin/python3
def max_integer(my_list=[]):
    a = sorted(my_list, reverse=True)
    if len(my_list) != 0:
        return(a[0])
    else:
        return(None)
