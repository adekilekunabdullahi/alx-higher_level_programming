#!/usr/bin/python3
"""Doc"""


def write_file(filename="", text=""):
    with open(filename, 'w', 'utf-8') as f:
        f.write(text)
