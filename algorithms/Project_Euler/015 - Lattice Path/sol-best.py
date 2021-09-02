"""
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке размером gridSize?
"""

import math


def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))



def solution(gridSize):
    """
    Возвращает количество путей, возможных в сетке n x n, начиная с верхнего левого угла, 
    переходя в нижний правый угол и имея возможность двигаться только вправо и вниз.

    >>> solution(20)
    137846528820
    >>> solution(1)
    2
    """
    return binomial(gridSize*2, gridSize)


if __name__ == "__main__":
    print(solution(int(input())))