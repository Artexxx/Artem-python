"""
Гугол ((10)^100) - гигантское число: один со ста нулями; (100)^100 почти невообразимо велико: один с двумястами нулями.
Несмотря на их размер, сумма цифр каждого числа равна всего лишь 1.

Рассматривая натуральные числа вида (a)^b, где a, b < 100, какая встретится максимальная сумма цифр числа?

  №     Время  Замедление      Аргумент    Результат
---  --------  ------------  ----------  -----------
  1  0.115326  11.533%              100          972 (Ответ)
  2  1.20859   109.326%             200         2205 <7515026 function calls>
"""


def fast_power(base, power, /):
    """
    Идея состоит в том, чтобы делить степень пополам на каждом шагу. т.к 3 ^ 10 = 9 ^ 5
    """
    result = 1
    while power != 0:
        if power % 2 == 0:
            power = power // 2
            base = base * base
        else:
            power = power - 1
            result = result * base

            power = power // 2
            base = base * base
    return result


def sum_of_digits(n):
    """
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(100000)
    1
    """
    s = 0
    while n != 0:
        n, last_digit = divmod(n, 10)
        s += last_digit
    return s


def solution(LIM=100):
    """
    Возвращает максимальную сумму цифр числа из чисел вида (a)^b, где a, b < `LIM`?
    """
    return max(sum_of_digits(fast_power(a, b))
               for a in range(0, LIM)
               for b in range(0, LIM))


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile;import cProfile
    TimeProfile(solution, [100, 200, 300])
    with cProfile.Profile() as pr:
        solution(200)
    pr.print_stats()