"""
Круговые простые числа
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?

  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
  1    1.508  150.800%      1000000           55
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


def is_circular_prime(n: int, n_is_prime: bool) -> bool:
    def rotations(chars: str) -> int:
        for i in range(len(chars)):
            yield int(chars[i:] + chars[:i])

    if not n_is_prime:
        return False

    for r in rotations(str(n)):
        if not is_prime(r): return False
    return True


def solution(N=1000000):
    """
    Возвращает количество круговых простых чисел меньше миллиона.

    >>> solution()
    55
    """
    sieve_bit_array = bit_sieve(N)
    return sum(1 for n in range(3, N, 2)
               if is_circular_prime(n, sieve_bit_array[n])) + 1

def f():
    N = 1000000
    prime = [False, False] + [True] * (N - 2)
    primes = []
    for p in range(2, N):
        if prime[p]:
            primes.append(p)
            for q in range(p * p, N, p):
                prime[q] = False
    count = 0
    pow10 = 1
    k_max = 1
    for p in primes:
        k = len(str(p))
        if k > k_max:
            pow10 *= 10
            k_max = k
        for i in range(k - 1):
            p = p // 10 + (p % 10) * pow10
            if not prime[p]:
                break
        else:
            count += 1
    print(count)

def x():
    bit_sieve(10 ** 6)
    return filter()
if __name__ == '__main__':
    import sys; sys.path.append('..')
    from time_profile import TimeProfile

    # TimeProfile(solution, [10 ** 6])
    TimeProfile(f)
