"""
Пан-цифровое простое число
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз.
К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?
    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0001417  0.014%                        7652413
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


def permutations(lst):
    if len(lst) == 0: yield []
    elif len(lst) == 1: yield lst
    for i in range(len(lst)):
        x = lst[i]
        xs = lst[:i] + lst[i + 1:]
        for p in permutations(xs):
            yield [x] + p


def solution():
    """
    Возращает нибольшее n-значное пан-цифровое простое число
    >>> solution()
    7652413
    """
    for perm_lst in permutations(list('7654321')):
        pandigital = int(''.join(perm_lst))
        if is_prime(pandigital):
            return pandigital


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)