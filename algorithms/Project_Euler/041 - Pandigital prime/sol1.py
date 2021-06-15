"""
Пан-цифровое простое число
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз.
К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?
"""
import sys; sys.path.append('../..')
from number_base_alg import is_prime


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
    print(solution())