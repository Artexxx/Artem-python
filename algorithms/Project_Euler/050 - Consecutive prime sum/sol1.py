"""
Сумма последовательных простых чисел
Простое число 41 можно записать в виде суммы шести последовательных простых чисел:

41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной сотни.

Самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.

Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего количества последовательных простых чисел?

   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  -----------
0.581774  58.177%                        997651 (Ответ)
"""
import math


def bit_sieve(n) -> list:
    """ Sieve of Eratosthenes
     Generate boolean array of length N, where prime indices are True.

    The time complexity of this algorithm is O(nloglog(n).

    >>> bit_sieve(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    primes = [True] * n
    primes[0], primes[1] = False, False  # числа 0 и 1

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[factor]:
            number_of_multiples = len(primes[factor * factor::factor * 2])
            primes[factor * factor::factor * 2] = [False] * number_of_multiples
    return primes


def get_primes(n):
    is_prime = bit_sieve(n)
    primes = [num for num in range(3, n + 1, 2) if is_prime[num]]
    return primes


def solution():
    """
    Находит простое число, меньше одного миллиона, которое можно записать в виде суммы наибольшего количества последовательных простых чисел.
    """
    primes = get_primes(10**6)
    longest = 21
    result = 0

    for i in range(len(primes)):
        for j in range(i + longest, len(primes) - i + 1):
            temp_sum = sum(primes[i:j])
            if temp_sum > 10**6:
                break
            if temp_sum in primes:
                if len(primes[i:j]) > longest:
                    result = temp_sum
                    longest = len(primes[i:j])

    return result


if __name__ == '__main__':
    # ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)
    import cProfile
    with cProfile.Profile() as pr:
       print(solution())
    print(pr.print_stats())