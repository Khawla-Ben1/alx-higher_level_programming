#!/usr/bin/python3
"""Multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """
    Args: Multiplies two matrices by using the module NumPy
        :param m_a: list of lists of integers or floats,
        :param m_b: list of lists of integers or floats.
    ValueError - if m_a, m_b is empty (it means: = [] or = [[]])
        or can’t be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    num_columns_m_a = 0
    num_rows_m_b = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if not isinstance(row1, list):
            raise TypeError("m_a must be a list of lists")
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len(row1) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        num_columns_m_a = len(row1)
        for column1 in row1:
            if not isinstance(column1, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if not isinstance(row2, list):
            raise TypeError("m_b must be a list of lists")
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len(row2) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        num_rows_m_b += 1
        for column2 in row2:
            if not isinstance(column2, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if num_columns_m_a != num_rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []
    for row_1 in m_a:
        column_index = 0
        row_result = []
        while column_index < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][column_index]
                k += 1
            row_result.append(result)
            column_index += 1
        mul_matrix.append(row_result)

    return mul_matrix
