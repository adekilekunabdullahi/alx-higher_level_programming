#!/usr/bin/python3
from sys import argv as av
def main():
    sums = 0
    for x in range(1, len(av)):
        sums += int(av[x])
    print(sums)
if __name__ == "__main__":
    main()
