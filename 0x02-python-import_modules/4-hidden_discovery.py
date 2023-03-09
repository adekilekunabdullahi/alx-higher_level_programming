#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    a = dir(hidden_4)
    for x in sorted(a):
        if x[0] != '_':
            print(x)
