#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return (None)
    if idx > len(my_list) - 1:
        return (None)
    else:
        new_list[idx] = element
        return new_list
