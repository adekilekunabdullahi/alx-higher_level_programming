#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
def main():
    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])
    array = {"+": add(a, b), "-": sub(a, b), "*": mul(a, b), "/": div(a, b)}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sign not in list(array.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        sums = 0
        for key, value in array.items():
            if sign == key:
                sums = array[key]
        print(f"{a} {sign} {b} = {sums}")
if __name__ == "__main__":
    main()
