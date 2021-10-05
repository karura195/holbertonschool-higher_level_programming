#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not any(isinstance(a, list) for a in matrix):
        raise TypeError(message)

    for i in range(len(matrix)):
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError(message)
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError(message2)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_list = []
        for n in row:
            new_list.append(round(n / div, 2))
        new_matrix.append(new_list)
    return new_matrix
