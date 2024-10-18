#!/usr/bin/python3
"""
Defines pasacal triangle that create list of lists
"""


def pascal_triangle(n):
    """
    defines triangle module
    """
    if n <= 0:
        return []
    temp = []
    prev_row = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(prev_row[j] + prev_row[j - 1])
        prev_row = row
        temp.append(row)
    return temp
