"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.

   n        Relatively Prime        φ(n)     n/φ(n)
   2        1                       1        2
   3        1,2                     2        1.5
   4        1,3                     2        2
   5        1,2,3,4                 4        1.25
   6        1,5                     2        3
   7        1,2,3,4,5,6             6        1.1666...
   8        1,3,5,7                 4        2
   9        1,2,4,5,7,8             6        1.5
   10       1,3,7,9                 4        2.5

Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.
Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
"""
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
    number_of_multiples = len(sieve[4::2])
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # number_of_multiples = len(sieve[factor * factor::2*factor]) # old code ─ slow version
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = zero * number_of_multiples
    return sieve


def prime_sieve(limit) -> Iterator[int]:
    sieve = bit_sieve(limit)
    yield 2
    yield from (i for i in range(3, limit, 2) if sieve[i])


def solution(limit=10 ** 6):
    """
    Возвращает значение n ≤ limit, при котором значение n/φ(n) максимально.
    """
    result = 1
    for prime in prime_sieve(int(math.sqrt(limit)) + 1):
        result *= prime
        if result * prime >= limit:
            return result


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10 ** 4, 10 ** 5, 10 ** 6])
