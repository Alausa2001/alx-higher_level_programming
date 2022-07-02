#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lists = dir(hidden_4)
    for a in lists:
        if a[0] == '_':
            pass
        else:
            print(a)
