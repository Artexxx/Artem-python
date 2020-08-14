"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

  №    Время  Замедление        Число         Результат
---  -------  ------------  ---------  ----------------
  1  2.1e-06   0.00%            10000          23331668
  2  1.4e-06  -0.00%           100000        2333316668
  3  1.2e-06  -0.00%          1000000      233333166668
  4  1e-06    -0.00%         10000000    23333331666668
  5  1e-06    -0.00%        100000000  2333333316666668
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
    sum = 0
    a = (number - 1) // 3
    b = (number - 1) // 5
    c = (number - 1) // 15
    sum += (a * (6 + (a - 1) * 3)) // 2
    sum += (b * (10 + (b - 1) * 5)) // 2
    sum -= (c * (30 + (c - 1) * 15)) // 2
    return sum


def solution(number):
    a = (number - 1) // 5
    b = (number - 1) // 3
    c = (number - 1) // 15
    sum_a = ((a * (a + 1)) // 2) * 5
    sum_b = ((b * (b + 1)) // 2) * 3
    sum_c = ((c * (c + 1)) // 2) * 15
    return sum_a + sum_b - sum_c


def solution(number):
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
