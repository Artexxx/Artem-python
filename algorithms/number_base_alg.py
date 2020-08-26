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


def sum_of_divisors(n):
    """Find the sum of divisors for the number

    >>> sum_of_divisors(220)
       284     #=>  sum(1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110)
    """
    total = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0 and i != sqrt(n):
            total += i + n // i
        elif i == sqrt(n):
            total += i
    return total - n


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


def bit_sieve_optimized(n) -> list:
    """ Решето Эратосфена.
    В списке primes сбрасываются биты, имеющие составные номера, биты с простыми номерами == True.
    i-му по порядку элементу будет соответствовать True, если i -- простое и False иначе.
    Сложность: nloglog(n).

    >>> bit_sieve_optimized(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    primes = [True] * n
    primes[0], primes[1] = False, False  # числа 0 и 1

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples
    for p in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[p]:
            number_of_multiples = len(primes[p * p::p * 2])
            primes[p * p::p * 2] = [False] * number_of_multiples  # занулить все ему кратные
    return primes
