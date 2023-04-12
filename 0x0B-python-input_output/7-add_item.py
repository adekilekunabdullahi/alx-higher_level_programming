#!/usr/bin/python3
"""Doc"""
import json
from sys import argv
save = __import__('5-save_to_json_file')
load = __import__('6-load_from_json_file')
lists = []
for x in range(len(argv)):
    if x == 0:
        continue
    lists.append(argv[x])
filename = "add_item.json"
save.save_to_json_file(lists, filename)
text = load.load_from_json_file(filename)
final_list = []

with open("add_item.json", 'a') as f:
    f.write(json.dumps(text))
