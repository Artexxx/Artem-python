"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше n.


  №      Время  Замедление      Аргумент       Результат
---  ---------  ------------  ----------  --------------
  1  0.0031426  0.314%            100000       454396537
  2  0.0310431  2.790%           1000000     37550402023
  3  0.310128   27.908%         10000000   3203324994356
  4  1.72953    141.940%        50000000  72619548630277
"""
import math


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
    sieve[0] = False
    sieve[1] = False
    number_of_multiples = len(sieve[4::2])
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            number_of_multiples = len(sieve[factor * factor::2*factor])
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def solution(limit: int) -> int:
    """
    Возвращает сумму всех простых чисел ниже limit.
    [*] Решето Эратосфена - один из самых эффективных способов найти все простые числа меньше n, когда n меньше 10 миллионов.

    >>> solution(2_000_000)
    142913828922
    >>> solution(1_000)
    76127
    >>> solution(7)
    10
    """
    sieve = bit_sieve(limit)
    prime_sum = 2
    for i in range(3, limit, 2):
        if sieve[i]:
            prime_sum += i
    return prime_sum


if __name__ == "__main__":
    # print(solution(int(input().strip())))
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [100_000, 1_000_000, 10_000_000, 50_000_000])
