#!/usr/bin/python3
"""Define a JSON string"""
import json


def to_json_string(my_obj):
    """Convert object strng to JSON string

    Args:
        my_obj - the object string
    """

    data = json.dumps(my_obj)

    return data
