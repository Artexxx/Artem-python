import numpy as np
from typing import List


def snail(matrix: List[List]) -> List:
    """
    Given an n x n matrix, return the array elements arranged from
    outermost elements to the middle element, traveling clockwise.

    >>> matrix = [[1,2,3],
    ...           [8,9,4],
    ...           [7,6,5]]
    >>> snail(matrix)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    result = []
    size = len(matrix)
    for n in range((size + 1) // 2):
        # Go right
        for i in range(n, size - n):
            result.append(matrix[n][i])
        # Go left
        for j in range(n + 1, size - n):
            result.append(matrix[j][- 1 - n])
        # Go down
        for i in range(n + 2, size - n + 1):
            result.append(matrix[- 1 - n][-i])
        # Go up
        for j in range(n + 2, size - n):
            result.append(matrix[-j][n])
    return result


test_matrix = [['a', 'b', 'c'],
               ['h', 'i', 'd'],
               ['g', 'f', 'e']]
print(snail(test_matrix))  # == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

test_matrix = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]
print(snail(test_matrix))  # == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# __________________________________________________________________________________________________________________________________

def zigzag_numpy(matrix: np.ndarray) -> np.ndarray:
    """
    Given an n x n array, return the array elements arranged from zig-zag - along the array's anti-diagonals.

    >>> matrix = [[1,2,6],
    ...          [3,5,7],
    ...          [4,8,9]]
    >>> zigzag_numpy(np.array(matrix))
    array([1., 3., 2., 6., 5., 4., 8., 7., 9.])
    """
    result = np.array([])

    matrix_fliplr = np.fliplr(matrix)
    matrix_flipud = np.flipud(matrix)

    for i in range(-matrix.shape[0], matrix.shape[1]):
        if i % 2 == 0:
            result = np.append(result, matrix_fliplr.diagonal(i * -1))
        else:
            result = np.append(result, matrix_flipud.diagonal(i * 1))

    return result


test_matrix = [[1, 3, 4],
               [2, 5, 8],
               [6, 7, 9]]
print(zigzag_numpy(np.array(test_matrix)))  # == np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


def zigzag(matrix: List[List]) -> List:
    """
    Given an n x n array, return the array elements arranged from zig-zag - along the array's anti-diagonals.

    >>> matrix = [[1,2,6],
    ...          [3,5,7],
    ...          [4,8,9]]
    >>> zigzag(matrix)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    columns, rows = len(matrix), len(matrix[0])
    mini_diagonals = [[] for _ in range(columns + rows - 1)]

    for x in range(columns):
        for y in range(rows):
            sum_indexes = x + y
            if sum_indexes % 2 == 0:
                mini_diagonals[sum_indexes].insert(0, matrix[x][y])
            else:
                mini_diagonals[sum_indexes].append(matrix[x][y])
    flatten = []
    for zig in mini_diagonals:
        flatten += zig
    return flatten


test_matrix = [[1, 3, 4],
               [2, 5, 8],
               [6, 7, 9]]
print(zigzag(test_matrix))  # == np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


# __________________________________________________________________________________________________________________________________

if __name__ == '__main__':
    import doctest
    doctest.testmod()