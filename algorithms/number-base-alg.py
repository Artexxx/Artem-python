import collections
import math
from math import sqrt


def gcd(a, b):
    """Computes the greatest common divisor of the integers a and b
    >>> gcd(12, 18)
    6
    """
    while b: a, b = b, a % b
    return abs(a)


def divisors(n) -> list:
    """Find the divisors for the number

    >>> divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220]
    """
    factors = list()
    sqrt_n = sqrt(n)
    for i in range(1, int(sqrt_n + 1)):
        if n % i == 0:
            factors.append(i)
            if i != sqrt_n:
                factors.append(n//i)
    return factors


def prime_factorization1(n):
    """Return a list of n's prime factors

    >>> factorint(220)
    [2, 2, 5, 11] # 2*2*5*11 == 220
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
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
def prime_factorization2(n):
    """Return a Counter dict of n's prime factors

     >>> prime_factorization2(220)
    {2: 2, 5: 1, 11: 1} # 2 * 2 * 5 * 11
    """
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            old_factorization = prime_factorization2(n / i).copy()
            old_factorization[i] += 1
            return old_factorization
    # Нет делителей -> x простое число
    res = collections.defaultdict(int)
    res[n] = 1
    return res


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
