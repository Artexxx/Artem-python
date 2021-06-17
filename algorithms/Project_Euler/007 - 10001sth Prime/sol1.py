"""
Выписав первые шесть простых чисел, получим

    2, 3, 5, 7, 11, 13

Какое число является N-ым простым числом?

  №       Время  Замедление      Аргумент    Результат
---  ----------  ------------  ----------  -----------
  1   0.0920908  9.209%             10001       104743 (ответ)
  2   2.86101    276.891%          100001      1299721
  3  92.5656     8970.461%        1000001     15485867
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

    >>> solution(10001)
    104743
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
    # print(solution(int(input().strip())))
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10001, 100001, 1000001])

