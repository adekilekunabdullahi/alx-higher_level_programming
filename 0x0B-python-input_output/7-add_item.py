#!/usr/bin/python3
"""Doc"""
import json
from sys import argv
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
lists = []
par = Path('./add_item.json')
if par.is_file():
    text = load_from_json_file(filename)
    for x in text:
        lists.append(x)
else:
    pass
for x in range(len(argv)):
    if x == 0:
        continue
    lists.append(argv[x])
save_to_json_file(lists, filename)
