#!/usr/bin/python3
"""
A python module that
implement a class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class implementation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """function width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ a width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y function getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """function area"""
        return self.__width * self.__height

    def display(self):
        """Function Display"""
        for i in range(self.__y):
            print()
        for x in range(self.__height):
            for y in range(self.__width):
                for k in range(self.__x):
                    if y >= 1:
                        continue
                    print(" ", end='')
                print("#", end='')
            print()

    def __str__(self):
        """function __str__"""
        return (f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """function updqtes"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """to_dictionary is a class that implement dictionary"""
        dicts = {
                'x': self.__x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
        return dicts
