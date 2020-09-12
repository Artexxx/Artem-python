"""
Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке,
образуется следующая спираль 5 на 5:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
"""


def spiralDiagonals(n):
    """Возращает сумму чисел в диагоналях спирали N на N.

    >>> spiralDiagonals(1001)
    669171001
    >>> spiralDiagonals(500)
    82959497
    >>> spiralDiagonals(100)
    651897
    >>> spiralDiagonals(50)
    79697
    >>> spiralDiagonals(10)
    537
    """
    solution = 1
    counter = 1
    increment = 2
    while (counter < n ** 2):
        for _ in range(4):
            counter += increment
            solution += counter
        increment += 2
    return solution


if __name__ == '__main__':
    print(spiralDiagonals(3))
