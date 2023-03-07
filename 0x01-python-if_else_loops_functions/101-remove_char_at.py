#!/usr/bin/python3
def remove_char_at(str, n):
    text = list(str)
    del text[n]
    text = str(text)
    return text
