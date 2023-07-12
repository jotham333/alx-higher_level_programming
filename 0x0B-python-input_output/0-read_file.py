#!/usr/bin/python3

"""Defines a read_file function"""


def read_file(filename=""):
    """Reads a text file

        Args:
            filename - The file name
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)
