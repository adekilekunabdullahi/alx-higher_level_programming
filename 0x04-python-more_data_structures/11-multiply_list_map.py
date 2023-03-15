#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    def multiply(x):
        return x * number
    new_list = my_list.copy()
    a = map(multiply, new_list)
    new_list2 = list(a)
    return new_list2
