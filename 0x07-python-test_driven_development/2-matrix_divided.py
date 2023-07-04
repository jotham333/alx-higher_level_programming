#!/usr/bin/python3
"""Defines an matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

          Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or any(not isinstance(row, list)
        for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                "integers/floats")

    # Check if each row of the matrix has the same size
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and rounding
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
