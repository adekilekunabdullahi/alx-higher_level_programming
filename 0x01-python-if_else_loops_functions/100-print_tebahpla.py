#!/usr/bin/python3
def reverse_alphabet():
    for x in reversed(range(97, 123)):
        if x % 2 == 0:
            print("{}".format(chr(x)), end="")
        else:
            print("{}".format(chr(x - 32)), end="")

reverse_alphabet()

