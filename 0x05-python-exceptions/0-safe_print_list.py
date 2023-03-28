#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for y in range(x):
            print(my_list[y], end='')
        print()
        return (x)
    except:
        print()
        x = 0
        for a in my_list:
            x += 1
        return x
