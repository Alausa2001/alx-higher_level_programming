#!/usr/bin/python3
def uniq_add(my_list=[]):
    sett = set(my_list)
    result = 0
    for elm in sett:
        result += elm
    return(result)
