"""
Круговые простые числа
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?

   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  -----------
0.0525863  5.259%       1000000              55
"""
import math


def bit_sieve(n) -> list:
    """
    Sieve of Eratosthenes
    Generate boolean array of length N, where prime indices are True.

    The time complexity of this algorithm is O(nloglog(n).

    >>> bit_sieve(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[factor]:
            number_of_multiples = len(primes[factor * factor::factor * 2])
            primes[factor * factor::factor * 2] = [False] * number_of_multiples
    return primes


SIEVE = bit_sieve(10 ** 6)


def is_circular_prime(n: int) -> bool:
    def rotations(chars: str) -> int:
        for i in range(len(chars)):
            yield int(chars[i:] + chars[:i])

    str_n = str(n)
    # Любая перестановка цифр числа должна быть простым числом —→
    # число не может содержать четные цифры 0, 2, 4, 6, 8, и цифру 5
    for digit in '50468':
        if digit in str_n:
            return False

    for r in rotations(str_n):
        if not SIEVE[r]:
            return False
    return True


def solution(limit):
    """
    Возвращает количество круговых простых чисел меньше.

    >>> solution(10**6)
    55
    """
    return sum(1 for n in range(101, limit, 2)
               if SIEVE[n] and is_circular_prime(n)) + 13


if __name__ == '__main__':
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10**6])
