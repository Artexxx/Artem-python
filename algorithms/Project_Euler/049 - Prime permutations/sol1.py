"""
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях:
    (1) каждый из трех членов является простым числом
    (2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел, демонстрирующих это свойство.
Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?

    Время  Замедление    Аргумент    Результат
---------  ------------  ----------  ----------------
0.0002929  0.029%                    296962999629 (Ответ)
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


def solution():
    def is_permutation(a, b):
        return sorted(str(a)) == sorted(str(b))

    primes = bit_sieve(10000)
    for num in range(1487+2, 10000-3330*2, 2):
        num_1 = num
        num_2 = num + 3330
        num_3 = num + 3330 + 3330

        if (primes[num_1] and
            primes[num_2] and
            primes[num_3] and
            is_permutation(num_1, num_2) and
            is_permutation(num_2, num_3)):
            return f"{num_1}{num_2}{num_3}"


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)