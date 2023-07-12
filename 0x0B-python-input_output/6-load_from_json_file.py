#!/usr/bin/python3
"""Define  load from json function"""


def load_from_json_file(filename):
    """
    Loads JSON data from a file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object represented by the JSON data.
    """
    with open(filename) as file:
        json_data = json.loads(fil)

    return json_data
