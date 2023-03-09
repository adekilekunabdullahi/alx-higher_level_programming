#!/usr/bin/python3
from sys import argv
def main():
    if len(argv) == 2:
        print("1 argument")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments".format(len(argv) - 1))
        for x in range(1, len(argv)):
            print("{}: {}".format(x, argv[x]))
if __name__ == "__main__":
    main()  
