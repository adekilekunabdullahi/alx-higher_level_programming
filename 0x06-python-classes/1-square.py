#!/usr/bin/python3
""" This code demonstrate
how to implement
classes
in
python
"""


class Square:
    """ a class Square that defines a square by: (based on 0-square.py)
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """Example of docstring on the __init__ method.
    The __init__ method may be documented in eithe      Args:
            size (:obj:`list` of :obj:`str`): Description of `param3`.
        """
        self.__size = size
