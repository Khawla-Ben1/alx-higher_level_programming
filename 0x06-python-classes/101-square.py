#!/usr/bin/python3
"""
Module 101-square
Defines a square class with a private instance attribute, property for size,
input validation, a private instance attribute for position, property for
position, input validation for position, a public instance method to calculate
the area, and a public instance method to print the square.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the new square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        The square is printed according to the position.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        The string representation should have the same behavior as the
        `my_print()` method.
        """
        if self.__size == 0:
            return ""
        square_str = ""
        for y in range(self.__position[1]):
            square_str += "\n"
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str.rstrip()
