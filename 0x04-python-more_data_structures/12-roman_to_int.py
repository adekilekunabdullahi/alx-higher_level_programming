#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for x in roman_string:
        if x not in values.keys():
            continue
        total += values[x]
    return total
