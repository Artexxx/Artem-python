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


def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
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
