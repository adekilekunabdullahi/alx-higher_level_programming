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
        if list_objs is None or list_objs == []:
            for x in list_objs:
                f = open(f"{cls.__name__}.json", 'w')
                f.write("[]")
                f.close()
        else:
            json_list = Base.to_json_string(x)
            f = open(f"{cls.__name__}.json", 'w')
            f.write(json_list)
            f.close()
