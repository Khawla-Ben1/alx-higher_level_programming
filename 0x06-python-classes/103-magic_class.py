#!/usr/bin/python3
import math
"""
Module 103-magic_class
Class MagicClass that does exactly the same as the following Python bytecode
"""


class MagicClass:
    """
    A class that represents a circle.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        area(): Calculates the area of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If `radius` is not a number (integer or float).
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
