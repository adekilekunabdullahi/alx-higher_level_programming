#!/usr/bin/python3
"""Doc"""


class BaseGeometry:
    """Doc"""
    def area(self):
        """Doc"""
        raise Exception("area() is not implemented")

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

    def area(self):
        """Doc"""
        return self.__width * self.__height

    def __str__(self):
        """Doc"""
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """Doc"""
    def __init__(self, size):
        """Doc"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Doc"""
        return self.__size * self.__size

    def __str__(self):
        """Doc"""
        return (f"[Rectangle] {self.__size}/{self.__size}")
