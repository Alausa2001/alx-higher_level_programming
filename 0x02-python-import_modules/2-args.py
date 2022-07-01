#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lists = (sys.argv)
    b = 1
    if len(lists) > 2:
        print("{} arguments".format(len(lists) - 1))
        for a in range(1, len(lists)):
            print(f"{a}", end=': ')
            print(lists[a])
    elif len(lists) == 2:
        print(f"{len(lists) - b} argument")
        for a in range(1, len(lists)):
            print(f"{a}", end=': ')
            print(lists[a])
    elif len(lists) == 1:
        print(f"{len(lists) - b} arguments")
