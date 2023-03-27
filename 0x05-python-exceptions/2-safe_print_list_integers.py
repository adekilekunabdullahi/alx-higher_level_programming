#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    try:
        for x in my_list:
            if type(x) == int:
                y += 1
                if y <= x:
                    print("{:d}".format(x), end='')
                else:
                    break
        return y
    except:
        return y
