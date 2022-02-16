"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n,
которые взаимно просты с n. К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9) = 6.
Число 1 считается взаимно простым для любого положительного числа, так что φ(1) = 1.

Интересно, что φ(87109) = 79180, и, как можно заметить, 87109 является перестановкой 79180.

Найдите такое значение n, 1<n<10^7, при котором φ(n) является перестановкой n, а отношение n/φ(n) является минимальным.

  №       Время  Замедление      Аргумент    Результат
---  ----------  ------------  ----------  -----------
  1   0.0731314  7.313%            100000        75841
  2   0.956609   88.348%          1000000       783169
  3  10.4914     953.475%        10000000      8319823
"""
from typing import List

import math
from typing import Iterator


def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, return boolean array of length `limit`,
    where index is number and boolean values is whether prime or not
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]

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
    sieve[0] = False
    sieve[1] = False
    # old code ─ slow version
    # # old code ─ slow version
    # number_of_multiples = len(sieve[4::2])
    number_of_multiples = (limit - 4 + limit % 2) // 2
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit + 1)) + 1, 2):
        if sieve[factor]:
            # old code ─ slow version
            # number_of_multiples = len(sieve[factor * factor::2*factor])
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def prime_sieve(limit) -> List[int]:
    """
    Input limit>=3, return a list of prime numbers less than `limit`.

    Example
    ========
    >>> prime_sieve(11)
    [2, 3, 5, 7, 11]
    >>> prime_sieve(17)
    [2, 3, 5, 7, 11, 13, 17]
    """
    from itertools import compress
    sieve = bit_sieve(limit+1)
    return [2, *compress(range(3, limit+1, 2), sieve[3::2])]


def has_same_digits(num1: int, num2: int) -> bool:
    """
    Return True if `num1` and `num2` have the same frequency of every digit, False otherwise.

    >>> has_same_digits(123456789, 987654321)
    True
    >>> has_same_digits(123, 23)
    False
    >>> has_same_digits(1234566, 123456)
    False
    """
    return sorted(str(num1)) == sorted(str(num2))


def solution(limit=10 ** 7):
    """
    Найдите такое значение n, 1 < n < `limit`, при котором φ(n) является
    перестановкой n, а отношение n/φ(n) является минимальным.

    >>> solution(100)
    21
    >>> solution(10000)
    4435
    """
    primes = prime_sieve(limit)
    count_primes = len(primes)
    min_numerator = 1
    min_denominator = 0

    for i in range(count_primes):
        for j in range(i+1, count_primes):
            p1, p2 = primes[i], primes[j]
            n = p1 * p2
            if n > limit:
                break
            # phi_n = p1*p2 * (1-1/p1) * (1-1/p1)
            phi_n = (p1 - 1) * (p2 - 1)
            if ((n * min_denominator < min_numerator * phi_n) and
                    has_same_digits(n, phi_n)):
                min_numerator = n
                min_denominator = phi_n
    return min_numerator


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    # TimeProfile(prime_sieve, [10 ** 5, 10 ** 6, 10 ** 7])
