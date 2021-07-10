import collections
import math
from math import sqrt
from typing import List, DefaultDict


def gcd(a, b, /) -> int:
    """Computes the greatest common divisor of the integers a and b
    >>> gcd(12, 18)
    6
    """
    while b: a, b = b, a % b
    return abs(a)


def divisors(number) -> List[int]:
    """Find the divisors for the number

    >>> divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220]
    """
    factors = list()
    sqrt_n = sqrt(number)
    for i in range(1, math.floor(sqrt_n + 1)):
        if number % i == 0:
            factors.append(i)
            if i != sqrt_n:
                factors.append(number // i)
    return sorted(factors)


def prime_factorization1(number) -> List[int]:
    """Return a list of n's prime factors

    >>> prime_factorization1(220) # 2*2*5*11 == 220
    [2, 2, 5, 11]
    """
    i = 2
    factors = []
    while i * i <= number:
        if number % i != 0:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


def memoize(f):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[#] F(",int(*args), ')\t => \t', dict(cache[args])) # TEST OUTPUT
        return cache[args]

    return wrapper


@memoize
def prime_factorization2(number) -> DefaultDict[int, int]:
    """Return a Counter dict of n's prime factors

     >>> prime_factorization2(220)
    {2: 2, 5: 1, 11: 1} # 2 * 2 * 5 * 11
    """
    sqrt_n = math.sqrt(number)
    for i in range(2, math.floor(sqrt_n + 1)):
        if number % i == 0:
            old_factorization = prime_factorization2(number // i).copy()
            old_factorization[i] += 1
            return old_factorization
    # No divisors -> x is a prime number
    res = collections.defaultdict(int)
    res[number] = 1
    return res


def is_prime(number) -> bool:
    """
    Determines if the natural number n is prime.

    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if number <= 3:
        return number > 1

    # check if multiple of 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    sqrt_n = math.sqrt(number)
    for i in range(5, math.floor(sqrt_n + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def bit_sieve(limit) -> List[bool]:
    """ Sieve of Eratosthenes
     Generate boolean array of length N, where prime indices are True.

    The time complexity of this algorithm is O(nloglog(n).

    >>> bit_sieve(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    primes = [True] * limit
    primes[0], primes[1] = False, False

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples
    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if primes[factor]:
            number_of_multiples = len(primes[factor * factor::factor * 2])
            primes[factor * factor::factor * 2] = [False] * number_of_multiples
    return primes


if __name__ == '__main__':
    import doctest

    doctest.testmod()
