#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_list = matrix.copy()
    new_matrix = []
    for x in new_list:
        a = []
        for y in x:
            b = y**2
            a.append(b)
        new_matrix.append(a)
    return new_matrix
