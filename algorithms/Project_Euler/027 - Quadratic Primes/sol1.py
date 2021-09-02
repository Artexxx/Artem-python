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
  1  0.0002734  0.027%                10          -21
  2  0.0186619  1.839%               100        -1455
  3  1.66361    164.495%            1000       -59231
"""
import math


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
    """ Возвращает произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное
        количество простых чисел для последовательных значений n, начиная с значения n=0.

    >>> solution(1000)
    -59231 # n^2 + an + b = n^2 - 61*n + 971
    """
    class result: n, a, b = 0, 0, 0

    for a in range(-LIMIT + 1, LIMIT):
        for b in range(-LIMIT, LIMIT + 1):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1

            if n > result.n:
                result.n = n
                result.a = a
                result.b = b

    print(f"n^2 + an + b = n^2{result.a:+}*n{result.b:+}")
    return result.a * result.b


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10, 100, 1000])
