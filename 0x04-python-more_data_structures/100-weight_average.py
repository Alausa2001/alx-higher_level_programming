#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted_total = 0
    weight = 0
    for i in my_list:
        weighted_total += i[0] * i[1]
        weight += i[1]
    return weighted_total / weight
