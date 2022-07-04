#!/usr/bin/python3
num = 122
for a in range(ord('y'), (ord('a') - 2), -1):
    print("{}".format(chr(num)), end='')
    if a % 2 == 0:
        num = (a)
    else:
        num = a - 32
