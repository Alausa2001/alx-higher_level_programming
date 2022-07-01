#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lists = (sys.argv)
    total = 0
    for a in range(1, len(lists)):
        total = total + int(lists[a])
    print(total)
