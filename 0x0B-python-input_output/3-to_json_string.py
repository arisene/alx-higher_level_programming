#!/usr/bin/python3
"""
Module 3 JSON
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of 
    an object (string):
    """
    s = json.dumps(my_obj)

    return s
