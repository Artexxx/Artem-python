"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше n, кратных 3 или 5.

  №    Время  Замедление        Число         Результат
---  -------  ------------  ---------  ----------------
  1  2.1e-06   0.00%            10000          23331668
  2  1.2e-06   0.00%          1000000      233333166668
  3  1e-06     0.00%        100000000  2333333316666668
"""


def solution(number):
    """ Возвращает сумму всех чисел, кратных 3 или 5 ниже n.
    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    def summ(number, d):
        n = (number - 1) // d
        return n * (n + 1) * d // 2

    return summ(number, 3) + summ(number, 5) - summ(number, 15)


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])
