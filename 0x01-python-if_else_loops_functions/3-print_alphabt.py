#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a == 113 or a == 101:
        pass
    else:
        print("{:c}".format(a), end='')
