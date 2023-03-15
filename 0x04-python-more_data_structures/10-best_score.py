#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for k in a_dictionary:
        if a_dictionary[k] == max(list(a_dictionary.values())):
            return k
