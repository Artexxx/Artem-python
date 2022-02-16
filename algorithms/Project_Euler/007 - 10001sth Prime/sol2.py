"""
Выписав первые шесть простых чисел, получим

    2, 3, 5, 7, 11, 13

Какое число является N-ым простым числом?

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0056097  0.561%             10001       104743 (ответ)
  2  0.0664887  6.088%            100001      1299721
  3  0.837998   77.151%          1000001     15485867
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
    # old code ─ slow version
    # number_of_multiples = len(sieve[4::2])
    number_of_multiples = (limit - 4 + limit % 2) // 2  # old code ─ slow version
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            number_of_multiples = len(sieve[factor * factor::2 * factor])
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(10001)
    104743
    """
    # N-ое простое не превосходит 1,5 N ln( N ) при N > 1:
    sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)

    count_primes = 0
    index = 1
    while count_primes != n and index < 3:
        index += 1
        if sieve[index]:
            count_primes += 1
    while count_primes != n:
        index += 2
        if sieve[index]:
            count_primes += 1
    return index


if __name__ == "__main__":
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10001, 100001, 1000001])
