#!/usr/bin/python3
"""
projects on classes in pythpn
"""


class Square:
    """
    a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """
        initiator
        """
        self.size = size

    @property
    def size(self):
        """
        pass
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        pass
        """
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        ...
        """
        return self.__size * self.__size
