#!/usr/bin/python3
def magic_calculation(a, b):
    return(98 + a ** b)
from dis import dis
dis(magic_calculation)
