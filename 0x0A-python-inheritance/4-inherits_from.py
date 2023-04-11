#!/usr/bin/python3
"""DOC"""


def inherits_from(obj, a_class):
    """Doc"""
    if issubclass(type(obj).__base__, a_class):
        return True
    return False
