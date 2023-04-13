#!/usr/bin/python3
"""
Defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        prev_row = triangle[-1]
        curr_row = [1]

        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i + 1])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
