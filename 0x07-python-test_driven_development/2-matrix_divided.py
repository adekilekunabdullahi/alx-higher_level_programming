#!/usr/bin/python3
"""
A program that divides each elements of a list
"""


def matrix_divided(matrix, div):
    """
    matrix_divided
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or (len(matrix) == 0)  or type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("""matrix must be a matrix\
 (list of lists) of integers/floats""")
    i = 0
    new_list = list()
    length = len(matrix[0])
    for x in matrix:
        if len(x) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_list_1 = []
        for y in x:
            if type(y) != float and type(y) != int:
                raise TypeError("""matrix must be a matrix\
 (list of lists) of integers/floats""")
            a = y / div
            new_list_1.append(round(a, 2))
        new_list.append(new_list_1)
    return (new_list)
