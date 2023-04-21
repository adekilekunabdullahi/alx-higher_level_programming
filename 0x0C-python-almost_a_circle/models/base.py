#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function to_json_string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function - save_to_file"""
        with open(f"{cls.__name__}.json", 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                x = [y.to_dictionary() for y in list_objs]
                f.write(cls.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        """ a static method that returns the list of the
        JSON string representation json_string:
        """
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)
