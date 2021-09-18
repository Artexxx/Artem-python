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
from math import log10

def memoization(f):
    memo = {}
    def helper(arg):
        if arg not in memo:
            memo[arg] = f(arg)
        return memo[arg]
    return helper

@memoization
def sqrtFrk(number):
    if number == 1:
        return 3, 2
    elif number == 2:
        return 7, 5
    else:
        return sqrtFrk(number - 1)[0] * 2 + sqrtFrk(number - 2)[0], sqrtFrk(number - 1)[1] * 2 + \
               sqrtFrk(number - 2)[1]

if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile;import cProfile
    TimeProfile(sqrtFrk, [1000])
    with cProfile.Profile() as pr:
        sqrtFrk(10000)
    pr.print_stats()

