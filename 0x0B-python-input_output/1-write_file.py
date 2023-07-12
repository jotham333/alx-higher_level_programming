#!/usr/bin/python3
"""Write a string into  file"""


def write_file(filename="", text=""):
    """write a string to a text file

        Args:
            filename - The file name
            Text - The string to write into the file

        Return: Returns the number of character written
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return (len(text))
