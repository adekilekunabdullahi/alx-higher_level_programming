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
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    summation = a + b
    return summation
