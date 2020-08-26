"""
Эйлер опубликовал свою замечательную квадратичную формулу:
	n^2+n+41

Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя значения 0≤n≤39.
 Однако, при n=40, 402+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно, при n=41,412+41+41 делится на 41 без остатка.
При помощи компьютеров была найдена невероятная формула n2−79n+1601, согласно которой можно получить 80 простых чисел для
последовательных значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:

	n^2+an+b
		где |a|<1000 и |b|≤1000
			где |a| является модулем (абсолютным значением) n.

Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество
простых чисел для последовательных значений n, начиная со значения n=0.


  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  9.52e-05   0.010%             10          -21
  2  0.0071047  0.70%             100        -1455
  3  0.808275   80.12%           1000       -59231
"""
import itertools, math


def is_prime(n: int) -> bool:
    """Determines if the natural number n is prime."""

    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3: return n > 1

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
    ''' Решето Эратосфена.
    В списке primes сбрасываются биты, имеющие составные номера, биты с простыми номерами == True.
    i-му по порядку элементу будет соответствовать True, если i -- простое и False иначе.
    Сложность: nloglog(n).

    >>> bit_sieve_optimized(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''
    primes = [True] * n
    primes[0], primes[1] = False, False  # числа 0 и 1

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples

    for p in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[p]:
            number_of_multiples = len(primes[p * p::p * 2])
            primes[p * p::p * 2] = [False] * number_of_multiples  # занулить все ему кратные
    return [i for (i, isprime) in enumerate(primes) if isprime]


def solution(LIMIT):
    """ Возращает произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное
        количество простых чисел для последовательных значений n, начиная со значения n=0.

    >>> solution(1000)
    -59231
    >>> solution(200)
    -4925
    """
    primesRange = bit_sieve_optimized(LIMIT)

    class solution:
        n = 0
        a = 0
        b = 0

    for i in range(0, len(primesRange)):
        b = primesRange[i]
        for a in range(LIMIT * -1 + 1, LIMIT):
            if not (b == 2 and a % 2 != 0):
                for n in itertools.count(1):
                    temp_prime_formula = n ** 2 + a * n + b
                    if not (temp_prime_formula in primesRange
                            or temp_prime_formula > primesRange[-1]
                            and is_prime(temp_prime_formula)
                    ):
                        break  # нам нужно n
                    # assert n > LIMIT
                if n > solution.n:
                    solution.n = n
                    solution.a = a
                    solution.b = b
    print(f"n^2 + an + b = n^2+{solution.a}*n+{solution.b}")
    return solution.a * solution.b


if __name__ == '__main__':
    # print(solution(1000))
    ### Run Time-Profile Table ###
    import sys;

    sys.path.append('..')
    from time_profile import my_time_this

    my_time_this(solution, [10, 100, 1000])
