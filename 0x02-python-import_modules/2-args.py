#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lists = (sys.argv)
    b = 1
    if len(lists) > 2:
        print("{} arguments:".format(len(lists) - 1))
        for a in range(1, len(lists)):
            print("{}".format(a), end=': ')
            print(lists[a])
    elif len(lists) == 2:
        print("{} argument:".format(len(lists) - 1))
        for a in range(1, len(lists)):
            print("{}".format(a), end=': ')
            print(lists[a])
    elif len(lists) == 1:
        print("{} arguments.".format(len(lists) - 1))
