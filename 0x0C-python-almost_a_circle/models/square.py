#!/usr/bin/python3
"""Python sc"""
from models import rectangle


class Square(rectangle.Rectangle):
    """Doc"""

    def __init__(self, size, x=0, y=0, id=None):
        """Doc"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Doc"""
        return self.width

    @size.setter
    def size(self, value):
        """Doc"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Doc"""
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
        """Doc"""
        return (f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}")

    def to_dictionary(self):
        """Doc"""
        dicts = {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.height}
        return dicts
