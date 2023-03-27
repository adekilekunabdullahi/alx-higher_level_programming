#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    try:
        for y in range(list_length):
            a = my_list_1[y] / my_list_2[y]
            lists.append(a)
    except ZeroDivisionError:
            a = 0
            lists.append(a)
            print("division by 0")
    except (TypeError, ValueError):
            a = 0
            lists.append(a)
            print("wrong type")
    except IndexError:
            print("out of range")
    finally:
            return lists


