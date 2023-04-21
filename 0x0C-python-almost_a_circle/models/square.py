#!/usr/bin/python3
"""square class implementation"""
from models import rectangle


class Square(rectangle.Rectangle):
    """Class square is inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """starter init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter function"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """instance method function"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.width = v
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def __str__(self):
        """str representation of the class"""
        return (f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}")

    def to_dictionary(self):
        """convert to dictionary method"""
        dicts = {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.height}
        return dicts
