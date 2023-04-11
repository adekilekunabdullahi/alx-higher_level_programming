#!/usr/bin/python3
"""Doc"""


class BaseGeometry:
    """Doc"""
    def area(self):
        """Doc"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Doc"""
    def __init__(self, width, height):
        """Doc"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
