#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = -1 * number
        last_digit = num % 10
        print(last_digit, end="")
        return last_digit
    else:
        num = number % 10
        print(num, end="")
