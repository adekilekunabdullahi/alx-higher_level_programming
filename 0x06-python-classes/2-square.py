#!/usr/bin/python3
""" This code show
classes
implementation in python
"""


class Square:
    """a class Square that defines a square by: (based on 1-square.py)
    """
    def __init__(self, size=0):
        """
        size: parameter
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
