#!/usr/bin/python3
"""Defines a function that append to a file"""


def append_write(filename="", text=""):
    """Appends a string to a file

    Args:
        filename - The name of the file
        text - the text string to append

    Return:
        Returns the number of character added
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return (len(text))
