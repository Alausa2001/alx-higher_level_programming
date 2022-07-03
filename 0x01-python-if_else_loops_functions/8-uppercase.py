#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = ord(a) - 32
        print("{}".format(chr(a)), end='')
    print()
