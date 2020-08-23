"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.

3
7 4
2 4 6
8 5 9 3

То есть, 3 + 7 + 4 + 9 = 23

Найдите максимальную сумму пути от вершины до основания следующего треугольника:

"""


def num_to_array(triangle):
    """
    3 становится [3], 7 становится [7]. Это немного облегчает суммирование чисел через строки треугольника,
    так как больше нет необходимости проверять, описывает ли предыдущая строка массив или целое число.
    """
    res = triangle.copy()
    for i in range(len(triangle)):
        for j, num in enumerate(triangle[i]):
            if num: res[i][j] = [num]
    return res


# Для каждого числа в array прибавляет currentValue
currentSum = lambda array, currentValue: [num + currentValue for num in array]


def maximumPathSumI(triangle):
    """Находит максимальную сумму в треугольнике, как описано в постановке задачи выше.

    >>> solution(triangle)
    1074
    """
    result_sum = num_to_array(triangle)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            current = result_sum[i][j]
            if (current):
                northWest = result_sum[i - 1][j - 1]
                northEast = result_sum[i - 1][j]

                result_sum[i][j] = []
                currentValue = current[0]
                if (northWest):
                    result_sum[i][j] = [*result_sum[i][j], *currentSum(northWest, currentValue)]
                if (northEast):
                    result_sum[i][j] = [*result_sum[i][j], *currentSum(northEast, currentValue)]
    flatten_result_sum = []
    for arr in result_sum[-1]:
        flatten_result_sum.extend(arr)
    return max(flatten_result_sum)


if __name__ == '__main__':
    # testTriangle = \
    #     [[3, 0, 0, 0],
    #      [7, 4, 0, 0],
    #      [2, 4, 6, 0],
    #      [8, 5, 9, 3]]
    # assert maximumPathSumI(testTriangle) == 23
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")
    with open(triangle, "r") as f: triangle = f.readlines()
    raw_triangle = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle]  # read row triangle
    triangle_with_zeros = [x + [0] * (len(raw_triangle[-1]) - len(x)) for x in raw_triangle]  # add zeros
    assert maximumPathSumI(triangle_with_zeros) == 1074
