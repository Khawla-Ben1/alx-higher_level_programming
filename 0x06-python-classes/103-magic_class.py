#!/usr/bin/python3
"""
Module 103-magic_class
Defines a class MagicClass that does exactly
the same as Python bytecode
"""


import math


class MagicClass:
    """
    A class that represents a circle.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        area(): Calculates the area of the circle.
    """

    def __init__(self, radius=1.0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (int or float, optional):
            The radius of the circle. Defaults to 1.0.

        Raises:
            TypeError: If `radius` is not a number (integer or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
