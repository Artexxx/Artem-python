"""
Given an n x n array, return the array elements arranged from
outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""


def snail(array):
    result = []

    if array and array[0]: size = len(array)
    for n in range((size + 1) // 2):

        """ go right """
        for i in range(n, size - n):
            result.append(array[n][i])
        """ go left """
        for j in range(n + 1, size - n):
            result.append(array[j][- 1 - n])
        """ go down """
        for i in range(n + 2, size - n + 1):
            result.append(array[- 1 - n][-i])
        """ go up """
        for j in range(n + 2, size - n):
            result.append(array[-j][n])

    return result


a = [['a', 'b', 'c'],
     ['h', 'i', 'd'],
     ['g', 'f', 'e']]
print(snail(a))  # == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

b = [[1, 2, 3, 4],
     [12, 13, 14, 5],
     [11, 16, 15, 6],
     [10, 9, 8, 7]]
print(snail(b))  # == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# __________________________________________________________________________________________________________________________________

import numpy as np


def rotateArr(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


# __________________________________________________________________________________________________________________________________


