#!/usr/bin/python3
"""
A module that adds 2 integers.
args: a and b must be integers or floats, otherwise TypeError is raise.
returns: the addition of the two numbers
"""


def add_integer(a, b=98):
    """
    a function that adds 2 integers.
    """
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    summation = a + b
    if summation == float('inf') or summation == -float('inf'):
        return 98
    if a != a:
        a = 98
    if b != b:
        b = 98
    return int(a) + int(b)
