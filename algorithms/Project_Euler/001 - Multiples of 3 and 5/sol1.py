"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше n, кратных 3 или 5.


  №      Время  Замедление        Число         Результат
---  ---------  ------------  ---------  ----------------
  1  0.0008558  0.086%            10000          23331668
  2  0.0090392  0.82%            100000        2333316668
  3  0.0944349  8.54%           1000000      233333166668
  4  0.950324   85.59%         10000000    23333331666668
  5  9.60341    865.31%       100000000  2333333316666668
"""


def solution(n):
    """
    Возвращает сумму всех чисел, кратных 3 или 5 ниже n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    """
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0])


if __name__ == "__main__":
    print(solution(int(input().strip())))

    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])
