#!/usr/bin/python3
"""Doc"""


def read_file(filename=""):
    """Doc"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
