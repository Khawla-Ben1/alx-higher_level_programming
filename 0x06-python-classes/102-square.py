#!/usr/bin/python3
"""
Module 102-square
Defines a square class with a private instance attribute, property for size,
input validation, a public instance method to calculate the area, and
comparative operators.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (float or int): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If `value` is not a number (float or integer).
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the current square is equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is equal
            to the other square, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the current square is not equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is not
            equal to the other square, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the current square is greater than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is greater
            than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the current square is
        greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is greater
            than or equal to the other square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the current square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is less than
            the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the current square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is
            less than or equal to the other square, False otherwise.
        """
        return self.area() <= other.area()
