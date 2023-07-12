#!/usr/bin/python3
"""Define a function that convert json file to python"""
import json


def from_json_string(my_str):
    """convert json file to python

    Args:
        my_str - The json string

    """

    data = json.loads(my_str)

    return data
