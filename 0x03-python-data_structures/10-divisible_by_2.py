#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if not my_list:
        return []
    else:
        for a in my_list:
            new.append(not(bool(a % 2)))
        return (new)
