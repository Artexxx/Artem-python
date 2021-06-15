"""
Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и удвоенного квадрата.
Оказалось, что данная гипотеза неверна.

 9 =  7 + 2×(1)^2
15 =  7 + 2×(2)^2
21 =  3 + 2×(3)^2
25 =  7 + 2×(3)^2
27 = 19 + 2×(2)^2
33 = 31 + 2×(1)^2

Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?

[#] Можно смотреть только нечётные числа.

    Время  Замедление      Число    Результат
---------  ------------  -------  -----------
0.0052454  0.525%              1         5777 (Ответ)
0.0001999  -0.505%          5777         5993
"""
import itertools
import math
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    """
    Determines if the natural number n is prime.

    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_goldbach(n):
    if n % 2 == 0 or is_prime(n):
        return True

    for i in itertools.count(1):
        k = n - 2 * i * i

        if k <= 0:
            return False

        elif is_prime(k):
            return True


def solution(start=1):
    """
    Находит следующее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата
    """
    for n in itertools.count(start=start, step=2):
        if not is_goldbach(n):
            return n



if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [3, 5779], DynamicTimer=True)
