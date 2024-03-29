#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    total = 0
    div = 0
    for x in my_list:
        total += (x[0] * x[1])
        div += x[1]
    return total/div
