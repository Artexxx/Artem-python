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
from typing import List


def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, return boolean array of length `limit`,
    where index is number and boolean values is whether prime or not
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    Time-Profile
    ============
    ===  =========  ============  ===========  ============
      №       Time  Slowdown         Argument  Count primes
    ===  =========  ============  ===========  ============
      1  0.001174   0.118%            100_000          9592
      2  0.013186   1.201%          1_000_000         78498
      3  0.131736   11.855%        10_000_000        664579
      4  1.63013    149.840%      100_000_000       5761455
    ===  =========  ============  ===========  ============
    """
    sieve = bytearray([True]) * limit
    zero = bytearray([False])

    sieve[0] = False
    sieve[1] = False
    # number_of_multiples = len(sieve[4::2]) # old code ─ slow version
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # number_of_multiples = len(sieve[factor * factor::2*factor]) # old code ─ slow version
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = zero * number_of_multiples
    return sieve


def prime_sieve(limit) -> List[int]:
    sieve = bit_sieve(limit)
    return [2] + [i for i in range(3, limit, 2) if sieve[i]]


def solution(LIMIT=10 ** 6):
    """
    Находит простое число, меньше одного миллиона, которое можно записать в виде суммы наибольшего количества последовательных простых чисел.
    """
    primes = prime_sieve(LIMIT)
    longest_len = 21
    result_sum = 0

    for i in range(len(primes)):
        for j in range(i + longest_len, len(primes) - i + 1):
            temp_sum = sum(primes[i:j])
            if temp_sum > LIMIT:
                break
            if temp_sum in primes and (j - i) > longest_len:
                result_sum = temp_sum
                longest_len = (j - i)
    return result_sum


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile

    TimeProfile(solution)
    import cProfile

    with cProfile.Profile() as pr:
        solution()
    print(pr.print_stats())
