#!/bin/python3
"""
A module that contains class declaration
"""


class Rectangle:
    """
    class Rectangle implementation
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width parameter getter function
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width parameter setter function
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def getter(self):
        """
        height parametter getter function
        """
        return self.__height

    def setter(self, value):
        """
        height parametter setter function
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    height = property(getter, setter,)
