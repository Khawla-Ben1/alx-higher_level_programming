#!/usr/bin/python3
"""
Module 3-square
Defines a square class with a private instance attribute, input validation,
and a public instance method to calculate the area of the square.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area.
        """
        return self.__size ** 2
