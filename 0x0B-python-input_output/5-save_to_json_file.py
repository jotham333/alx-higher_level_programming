#!/usr/bin/python3
"""Define a jason file"""
import json


def save_to_json_file(my_obj, filename):
    """Save an Object using jason representation

    Args:
        my_obj - The object
        filename - the file

    Return: The jason representation

    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
