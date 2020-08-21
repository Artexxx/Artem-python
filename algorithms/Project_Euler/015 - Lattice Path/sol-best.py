"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import math


def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))



def solution(gridSize):
    """
    Возвращает количество путей, возможных в сетке n x n, начиная с верхнего левого угла, 
    переходя в нижний правый угол и имея возможность двигаться только вправо и вниз.

    >>> solution(25)
    126410606437752
    >>> solution(23)
    8233430727600
    >>> solution(20)
    137846528820
    >>> solution(15)
    155117520
    >>> solution(1)
    2
    """
    return binomial(gridSize*2, gridSize)


if __name__ == "__main__":
    print(solution(int(input())))