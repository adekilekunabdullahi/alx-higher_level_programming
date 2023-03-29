#!/usr/bin/python3
"""
This code shows classes in python
"""


class Square:
    """
    a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """
        function called when initiated
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        function that return the area of the square
        """
        return self.__size * self.__size
