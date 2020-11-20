"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.

3
7 4
2 4 6
8 5 9 3

То есть, 3 + 7 + 4 + 9 = 23

Найдите максимальную сумму пути от вершины до основания следующего треугольника:
"""


def solution(triangle):
    """Находит максимальную сумму в треугольнике, как описано в постановке задачи выше.

    >>> solution(triangle)
    1074
    """
    for row in reversed(range(len(triangle) - 1)):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]


if __name__ == "__main__":
    # testTriangle = \
    #     [[3],
    #      [7, 4],
    #      [2, 4, 6],
    #      [8, 5, 9, 3]]
    # assert solution(testTriangle) == 23
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")
    with open(triangle, "r") as f: triangle = f.readlines()
    triangle = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle]
    print(solution(triangle))
