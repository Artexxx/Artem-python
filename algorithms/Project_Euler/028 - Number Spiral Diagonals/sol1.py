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

from math import ceil


def diagonal_sum(n):

    """Возращает сумму чисел в диагоналях спирали N на N.

    >>> diagonal_sum(1001)
    669171001
    >>> diagonal_sum(500)
    82959497
    >>> diagonal_sum(100)
    651897
    >>> diagonal_sum(50)
    79697
    >>> diagonal_sum(10)
    537
    """
    total = 1

    for i in range(1, int(ceil(n / 2.0))):
        odd = 2 * i + 1
        even = 2 * i
        total = total + 4 * odd ** 2 - 6 * even

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(diagonal_sum(1001))
    else:
        try:
            n = int(sys.argv[1])
            print(diagonal_sum(n))
        except ValueError:
            print("Invalid entry - please enter a number")
