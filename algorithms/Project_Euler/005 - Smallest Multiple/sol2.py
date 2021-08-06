"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до N?

  №     Время  Замедление      Число                                   Результат
---  --------  ------------  -------  ------------------------------------------
  1  1.04e-05  0.001%             10                                        2520
  2  2.04e-05  0.00%              15                                      240240
  3  2.37e-05  0.00%              20                                   232792560
  4  2.83e-05  0.00%              25                                  7138971840
  5  3.16e-05  0.00%              50                       354176514770971052160
  6  3.13e-05  0.00%             100  793262935946950851294251337219553320468480
"""

import math


def prime_factors(x) -> list:
    """ Возвращает простые чисела, образующие х

    >>> prime_factors(24)
    [2, 2, 2, 3]
    """
    if x <= 1: return []
    for i in range(2, x + 1):
        if x % i == 0:
            return [i, *prime_factors(x // i)]


def primes_frequency(primes: list) -> list:
    """"Возвращает частоты последовательных простых чисел

    >>> primes_frequency([2, 2, 3, 3, 2, 3])
    [[2, 2], [3, 2], [2, 1], [3, 1]]
    """
    frequency = [[primes[0], 1]]

    for i in range(1, len(primes)):
        if primes[i] != primes[i - 1]:
            frequency.append([primes[i], 1])
        else:
            frequency[-1][1] += 1
    return frequency


def primes_greatest_frequency(primes_frequency_list: list) -> dict:
    """Возвращает самые большие частоты последовательных простых чисел

    >>> primes_greatest_frequency([2, 2])
    { 2: 2, 3: 2 }
    """
    max_frequency = {}
    for frequency in primes_frequency_list:
        value = max_frequency.get(frequency[0])
        if value:
            max_frequency[frequency[0]] = max(value, frequency[1])
        else:
            max_frequency[frequency[0]] = frequency[1]
    return max_frequency


def solution(n):
    """Возвращает наименьшее положительное число, которое равномерно делится (без остатка) на все числа от 1 до n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    """
    primes = []
    for i in range(n, 1, -1):
        primes.extend(prime_factors(i))
    primes_frequency_list = primes_frequency(primes)
    max_frequency = primes_greatest_frequency(primes_frequency_list)

    result_number = 1
    for item in max_frequency.items():
        result_number *= math.pow(*item)
    return result_number


if __name__ == '__main__':
    print(solution(20))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10, 15, 20, 25, 50, 100])
