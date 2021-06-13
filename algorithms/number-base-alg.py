import math
from math import sqrt


def gcd(a, b):
    """Computes the greatest common divisor of the integers a and b
    >>> gcd(12, 18)
        6
    """
    while b: a, b = b, a % b
    return abs(a)


def sum_of_divisors_range(LIMIT) -> list:
    """Find the sum of proper divisors for each number"""
    sum_of_divisors = [0] * LIMIT
    for i in range(1, len(sum_of_divisors)):
        for j in range(i * 2, len(sum_of_divisors), i):
            sum_of_divisors[j] += i
    return sum_of_divisors


def divisors(n):
    """Find the divisors for the number

    >>> divisors(220)
       284     #=> [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    """
    factors = set()
    sqrt_n = sqrt(n)
    for i in range(1, int(sqrt_n + 1)):
        if n % i == 0:
            factors.add(i)
            if i != sqrt(n):
                factors.add(n//i)
    return factors


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
