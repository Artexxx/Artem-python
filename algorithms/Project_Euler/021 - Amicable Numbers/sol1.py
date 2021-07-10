"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.

  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0001212  0.012%            100            0
  2  0.0020599  0.19%            1000          504
  3  0.047425   4.54%           10000        31626
  4  1.20486    115.74%        100000       852810
"""
from math import sqrt


def sum_of_divisors(n):
    total = 0
    for i in range(1, int(sqrt(n) + 1)):
        if (n % i) == 0:
            total += i + (n // i)
    return total - n


def solution(LIMIT):
    """Возвращает сумму всех дружественных чисел (m, n) ниже LIMIT.

    >>> solution(10000)
    31626
    >>> solution(5000)
    8442
    >>> solution(1000)
    504
    >>> solution(100)
    0
    """
    total = 0
    for m in range(2, LIMIT):
        n = sum_of_divisors(m)

        # M и N удовлетворяют условиям дружественных пар:  m < n < LIMIT
        if (m < n < LIMIT) and sum_of_divisors(n) == m:
            total += m + n
    return total


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [100, 1000, 10_000, 100_000])
