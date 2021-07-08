"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:

    1,2,3,5,8,13,21,34,55,89,..

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают n.

  №     Время  Замедление                       Число                Результат
---  --------  ------------  ------------------------  -----------------------
  1  1.4e-06   0.001%           100000000000000000000     67650926172353373024
  2  1.5e-06  -0.001%          1000000000000000000000   1213946614199987541226
  3  1.6e-06   0.00%          10000000000000000000000   5142360378806858706956
  4  1.5e-06   0.00%         100000000000000000000000  92275912896516548183166
"""

import math
from decimal import Decimal, getcontext


def solution(n):
    """ Возвращает сумму всех четных чисел ряда Фибоначчи, которые ниже или равны n.

    >>> solution(10)
    10
    >>> solution(2)
    2
    >>> solution(1)
    0
    """
    getcontext().prec = 100
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2)

    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2)
    sum = num // 2
    return int(sum)


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [100_000_000_000_000_000_000, 1_000_000_000_000_000_000_000, 10_000_000_000_000_000_000_000, 100_000_000_000_000_000_000_000])
