#!/usr/bin/python3
"""
...
"""


class Square:
    """
    ...
    """
    def __init__(self, size=0):
        """
        pass
        """
        self.size = size

    @property
    def size(self):
        """
        ...
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        ...
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

    def my_print(self):
        """
        ...
        """
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print('#', end="")
                print()
