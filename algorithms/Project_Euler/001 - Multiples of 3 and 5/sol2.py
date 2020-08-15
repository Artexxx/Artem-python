"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше n, кратных 3 или 5.

  №       Время  Замедление        Число         Результат
---  ----------  ------------  ---------  ----------------
  1   0.0010031  0.1%              10000          23331668
  2   0.0085769  0.76%            100000        2333316668
  3   0.108283   9.97%           1000000      233333166668
  4   1.01057    90.23%         10000000    23333331666668
  5  10.8294     981.88%       100000000  2333333316666668
"""


def solution(n):
    """ Возвращает сумму всех чисел, кратных 3 или 5 ниже n.
    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    """
    xmulti = []
    zmulti = []
    z = 3
    x = 5
    temp = 1
    while True:
        result = z * temp
        if result < n:
            zmulti.append(result)
            temp += 1
        else:
            temp = 1
            break
    while True:
        result = x * temp
        if result < n:
            xmulti.append(result)
            temp += 1
        else:
            break
    collection = list(set(xmulti + zmulti))
    return sum(collection)


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])
