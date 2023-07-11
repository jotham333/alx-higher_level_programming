#!/usr/bin/python3

"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):

        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return (self.__size**2)
