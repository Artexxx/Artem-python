"""
Кратные из переставленных цифр Body:
Найдите такое наименьшее натуральное число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.

    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0433929  4.339%                         142857
"""
import itertools


def is_permuted(a, b):
    return sorted(str(a)) == sorted(str(b))


def solution():
    """
    Находит наименьшее натуральное число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.
    """
    for x in itertools.count(start=1002, step=3):
        if (is_permuted(x, x * 2) and
            is_permuted(x, x * 3) and
            is_permuted(x, x * 4) and
            is_permuted(x, x * 5) and
            is_permuted(x, x * 6)):
            return x


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)