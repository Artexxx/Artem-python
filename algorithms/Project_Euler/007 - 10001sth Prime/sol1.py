"""
Выписав первые шесть простых чисел, получим

    2, 3, 5, 7, 11, 13

Какое число является N-ым простым числом?

  №     Время  Замедление      Число    Результат
---  --------  ------------  -------  -----------
  1  0.246657  24.666%         20000       224737
  2  0.694757  44.81%          40000       479909
  3  1.95447   125.97%         80000      1020379
  4  3.67302   171.85%        120000      1583539
"""
from math import sqrt


def is_prime(n):
    if n == 2: return True
    elif n % 2 == 0: return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0: return False
    return True


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(100)
    541
    """
    count_primes = 0
    index = 1
    while count_primes != n and index < 3:
        index += 1
        if is_prime(index):
            count_primes += 1
    while count_primes != n:
        index += 2
        if is_prime(index):
            count_primes += 1
    return index


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [20_000,  40_000,  80_000, 120_000])
