#!/usr/bin/python3
"""Doc"""


def append_write(filename="", text=""):
    """Doc"""
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
        return num
