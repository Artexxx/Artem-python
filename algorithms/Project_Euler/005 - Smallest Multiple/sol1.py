"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до N?

  №     Время  Замедление      Число                                   Результат
---  --------  ------------  -------  ------------------------------------------
  1  9.6e-06   0.001%             10                                        2520
  2  1.04e-05  0.00%              15                                      240240
  3  1.37e-05  0.00%              20                                   232792560
  4  1.83e-05  0.00%              25                                  7138971840
  5  4.16e-05  0.00%              50                       354176514770971052160
  6  7.13e-05  0.00%             100  793262935946950851294251337219553320468480
"""
import math


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


def primes_mutiples_until(end):
    """
    Разделяет все числа от [1 до end] на простые и составные.

    >>> primes_mutiples_until(8)
    ([2, 3, 5, 7], [4, 6, 8])
    """
    primes, multiples = [], []
    for i in range(2, end + 1):
        if is_prime(i):
            primes.append(i)
        else:
            multiples.append(i)
    return primes, multiples


def solution(end):
    """Возвращает наименьшее положительное число, которое равномерно делится (без остатка) на все числа от 1 до n.
    [*] В основе лежит фундаментальная арифметическая теорема

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    """
    the_number = 1
    primes, multiples = primes_mutiples_until(end)

    for p in primes:
        the_number *= p

    for m in multiples:
        reminder = the_number % m
        if reminder != 0:
            if is_prime(reminder):
                the_number *= reminder
            else:
                for p in primes:
                    if reminder % p == 0:
                        the_number *= p
                        break
    return the_number


if __name__ == '__main__':
    end = 20
    print(solution(end))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10, 15, 20, 25, 50, 100])
