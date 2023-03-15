#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary):
        y = a_dictionary[str(x)]
        print(f"{x}: {y}")
