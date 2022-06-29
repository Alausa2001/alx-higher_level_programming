#!/usr/bin/python3
for a in range(0, 8):
    for b in range(0, 10):
        if b > a:
            print("{}".format(a), end='')
            print("{}".format(b), end=', ')
print("{}{}".format(a + 1, b))
