"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше n.


  №       Время  Замедление      Число     Результат
---  ----------  ------------  -------  ------------
  1   0.0051545  0.515%          10000       5736396
  2   0.0862083  8.11%          100000     454396537
  3   1.90828    182.21%       1000000   37550402023
  4  18.3567     1644.84%      5000000  838596693108
"""
from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0: return False
    return True


def sum_of_primes(n):
    if n > 2: sumOfPrimes = 2
    else: return 0
    for candidate in range(3, n, 2):
        if is_prime(candidate):
            sumOfPrimes += candidate
    return sumOfPrimes


def solution(n):
    """Возвращает сумму всех простых чисел ниже n.

    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """
    return sum_of_primes(n)


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10_000, 100_000, 1_000_000, 5_000_000])
