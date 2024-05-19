#!/usr/bin/python3
"""
Module 1-square
Defines a square class with a private instance attribute.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
