#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """
    Args: Prints a square with the character 'x'
        :param size: length of the square (must be an integer).
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("x", end='')
        print()
