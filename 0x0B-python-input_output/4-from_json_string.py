#!/usr/bin/python3
"""
Module 3 JSON
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    s = json.loads(my_str)

    return s
