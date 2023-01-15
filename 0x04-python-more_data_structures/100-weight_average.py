#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_total = 0
    weight = 0
    for i in my_list:
        weighted_total += i[0] * i[1]
        weight += i[1]
    return weighted_total / weight
