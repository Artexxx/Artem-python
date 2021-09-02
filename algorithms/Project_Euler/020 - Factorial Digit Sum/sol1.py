"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе n!.

  №       Время  Замедление     Число    Результат
---  ----------  ------------ -------  -----------
  1   4.24e-05   0.004%           100          648
  2   0.0029291  0.29%           1000        10539
  3   0.431312   42.84%         10000       149346
  4   7.3457     891.43%        50000       903555
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


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


def solution(n):
    """Возвращает сумму цифр в числе n!
    >>> solution(100)
    648 #9332621544...0000
    >>> solution(5)
    3 #120
    >>> solution(3)
    6 #6
    """
    f = factorial(n)
    result = sum_of_digits(f)
    return result


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [100, 1000, 10_000, 100_000])
