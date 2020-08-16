"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до N?


  №     Время  Замедление      Число                            Результат
---  --------  ------------  -------  -----------------------------------
  1  7.2e-06   0.001%             10                                 2520
  2  7.2e-06   0.00%              15                               360360
  3  9.9e-06   0.00%              20                            232792560
  4  1.2e-05   0.00%              25                          26771144400
  5  1.94e-05  0.00%              40                     5342931457063200
  6  4.28e-05  0.00%              80  32433859254793982911622772305630400
"""

def gcd(x, y):
    """ Euclidean GCD Algorithm """
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    """ Using the property lcm*gcd of two numbers = product of them """
    return (x * y) // gcd(x, y)


def solution(n):
    """Возвращает наименьшее положительное число, которое равномерно делится (без остатка) на все числа от 1 до n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    """
    g = 1
    for i in range(1, n + 1):
        g = lcm(g, i)
    return g



if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10, 15, 20, 25, 40, 80])