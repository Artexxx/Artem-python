"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше n.


  №      Время  Замедление       Число       Результат
---  ---------  ------------  --------  --------------
  1  0.0055752  0.558%          100000       454396537
  2  0.0673298  6.18%          1000000     37550402023
  3  0.923934   85.66%        10000000   3203324994356
  4  4.993      406.91%       50000000  72619548630277
"""
import math

def bit_sieve(n) -> list:
    ''' Решето Эратосфена.
    В списке bits сбрасываются биты, имеющие составные номера, биты с простыми номерами == 1.
    i-му по порядку элементу будет соответствовать 1, если i -- простое и 0 иначе.

    Сложность: nloglog(n).
    '''
    bits = [1] * (n + 1)
    for index in range(2, int(math.sqrt(n))):
        if bits[index]:  # если i -- простое
            for j in range(index * index, n + 1, index):  # занулить все ему кратные
                bits[j] = 0
    return bits

def bit_sieve_optimized(n) -> list:
    """ Оптимизированное Решето Эратосфена. """
    primes = [True] * n
    primes[0], primes[1] = False, False  # числа 0 and 1

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples

    for p in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[p]:
            number_of_multiples = len(primes[p * p::p * 2])
            primes[p * p::p * 2] = [False] * number_of_multiples  # занулить все ему кратные
    return primes


def prime_sum(n: int) -> int:
    """Возвращает сумму всех простых чисел ниже n.
    [*] Решето Эратосфена - один из самых эффективных способов найти все простые числа меньше n, когда n меньше 10 миллионов.

    >>> prime_sum(2_000_000)
    142913828922
    >>> prime_sum(1_000)
    76127
    >>> prime_sum(5_000)
    1548136
    >>> prime_sum(10_000)
    5736396
    >>> prime_sum(7)
    10
    """
    list_of_primality = bit_sieve_optimized(n)
    return sum((i for (i, isprime) in enumerate(list_of_primality) if isprime))

if __name__ == "__main__":
    # print(prime_sum(int(input().strip())))
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import my_time_this
    my_time_this(prime_sum, [100_000, 1_000_000, 10_000_000, 50_000_000])
