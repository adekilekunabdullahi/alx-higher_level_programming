#!/usr/bin/python3
"""Doc"""
import json


def load_from_json_file(filename):
    """Doc"""
    with open(filename, 'r') as f:
        text = f.read()
        return json.loads(text)
