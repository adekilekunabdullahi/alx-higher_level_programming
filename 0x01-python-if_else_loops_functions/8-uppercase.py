#!/usr/bin/python3
def uppercase(str):
    for x in str:
        c = ord(x)
        if c >= 97 and c <= 122:
            c -= 32
        print(f"{chr(c)}", end="")
    print("")
