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
            raise ValueError(f"{name} must be greater than 0")
