"""
Выписав первые шесть простых чисел, получим

    2, 3, 5, 7, 11, 13

Какое число является N-ым простым числом?


  №     Время  Замедление      Число    Результат
---  --------  ------------  -------  -----------
  1  0.652925  65.293%        200000      2750125
  2  0.99529   34.24%         300000      4256193
  3  1.36281   36.75%         400000      5800051
  4  2.15794   79.51%         600000      8960445
"""
import itertools
import math
import math


def bit_sieve(n):
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


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(100)
    541
    """
    # N-ое простое не превосходит 1,5 N ln( N ) при N > 1:
    sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)
    index = 0
    while n:
        n -= sieve[index]
        index += 1
    return index + 1


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [200_000, 300_000, 400_000, 600_000])
