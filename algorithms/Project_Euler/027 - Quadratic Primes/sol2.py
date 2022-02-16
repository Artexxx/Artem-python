"""
Эйлер опубликовал свою замечательную квадратичную формулу:
	n^2+n+41

Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя значения 0≤n≤39.
 Однако, при n=40, 402+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно, при n=41,412+41+41 делится на 41 без остатка.
При помощи компьютеров была найдена невероятная формула n2−79n+1601, согласно которой можно получить 80 простых чисел для
последовательных значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:
    n^2+an+b
    Где 1. |a|<1000 и |b|≤1000
	    2. |a| является модулем (абсолютным значением) n.

Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество
простых чисел для последовательных значений n, начиная со значения n=0.


  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0001656  0.017%                10          -21
  2  0.0072277  0.706%               100        -1455
  3  0.390135   38.291%             1000       -59231 <Ответ>
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
    # number_of_multiples = len(sieve[4::2]) # old code ─ slow version
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # number_of_multiples = len(sieve[factor * factor::2*factor]) # old code ─ slow version
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def prime_sieve(limit) -> Iterator[int]:
    sieve = bit_sieve(limit)
    yield 2
    yield from (i for i in range(3, limit, 2) if sieve[i])


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


def solution(LIMIT):
    """
    Возвращает произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное
    количество простых чисел для последовательных значений n, начиная с значения n=0.

    >>> solution(1000)
    -59231 # n^2 + an + b = n^2 - 61*n + 971
    """

    class result:
        n, a, b = 0, 0, 0

    for a in range(-LIMIT + 1, LIMIT):
        if a % 2 == 0:
            continue

        for b in prime_sieve(LIMIT):
            n = 0
            while is_prime(n * (n + a) + b):
                n += 1

            if n > result.n:
                result.n = n
                result.a = a
                result.b = b

    print(f"n^2 + an + b = n^2{result.a:+}*n{result.b:+}")
    return result.a * result.b


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;

    sys.path.append('..')
    from time_profile import TimeProfile

    TimeProfile(solution, [10, 100, 1000])
