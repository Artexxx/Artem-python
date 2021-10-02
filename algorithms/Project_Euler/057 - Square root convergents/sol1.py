"""
Приближения квадратного корня
Можно убедиться в том, что квадратный корень из двух можно выразить в виде бесконечно длинной дроби.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

Приблизив это выражение для первых четырех итераций, получим:
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985, является первым случаем, в котором количество цифр в числителе превышает количество цифр в знаменателе.

У скольких дробей длина числителя больше длины знаменателя в первой тысяче приближений выражения?

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0006408  0.064%              1000          153  Ответ
  2  0.0144547  1.381%             10000         1508 <20000 function calls>
"""
from math import log10, gcd


def solution(LIM=1000):
    """
    Возвращает количество дробей в которых длина числителя больше длины знаменателя в первой тысяче приближений

    Идея: https://en.wikipedia.org/wiki/Continued_fraction
    Согласно ссылке, если p/q является первым приближением, то следующее приближение может быть записано как (p+2q)/(p+q).
    Итак, начнем с 3/2 (первое приближение для √2), где p = 3 и q = 2

    >>> solution(1000)
    153
    """
    result = 0
    numerator = 3
    denominator = 2

    for _ in range(LIM):
        numerator = numerator + denominator * 2
        denominator = numerator - denominator

        if int(log10(numerator)) > int(log10(denominator)):
            result += 1
    return result


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile;import cProfile
    TimeProfile(solution, [1000, 10000])
    with cProfile.Profile() as pr:
        solution(10000)
    pr.print_stats()

