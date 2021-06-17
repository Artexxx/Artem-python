"""
Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:

14 = 2 × 7
15 = 3 × 5

Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Найдите первые четыре последовательных числа, каждое из которых имеет четыре отличных друг от друга простых множителя. Каким будет первое число?

  Время  Замедление    Аргумент      Результат
-------  ------------  ----------  ----------- <913330 function calls>
1.33932  133.932%               4       134043 (Ответ)
"""
import math


def memoize(f):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[#] F(",int(*args), ')\t => \t', dict(cache[args])) # TEST OUTPUT
        return cache[args]

    return wrapper

@memoize
def prime_factors(n) -> set:
    """Return a set of n's prime factors

    >>> prime_factors(220)
    [2, 5, 11]
    """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def solution(start=1):
    """Находит первое из первых четырех последовательных чисел, каждое из которых имеет четыре отличных друг от друга простых множителя.
    """
    number = start
    while True:
        if      len(prime_factors(number)) == 4\
            and len(prime_factors(number + 1)) == 4 \
            and len(prime_factors(number + 2)) == 4 \
            and len(prime_factors(number + 3)) == 4:
            break
        number += 1
    return number


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    import cProfile
    with cProfile.Profile() as pr:
        TimeProfile(solution, [1, 134043+1, 238203+1])
    pr.print_stats()

