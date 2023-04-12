#!/usr/bin/python3
"""Doc"""
import json
from sys import argv
save = __import__('5-save_to_json_file')
load = __import__('6-load_from_json_file')
filename = "add_item.json"
lists = []
text = load.load_from_json_file(filename)
for x in text:
    lists.append(x)
for x in range(len(argv)):
    if x == 0:
        continue
    lists.append(argv[x])
save.save_to_json_file(lists, filename)
