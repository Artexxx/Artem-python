"""

Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
"""


def sum_digit_power(number, degree) -> int:
    """
    Возвращает сумму циф числа `number`, которые были возведены в степень `degree`

    >>> sum_digit_power(4151)
    4151 #=> sum(1024, 1, 3125, 1)
    """
    return sum(pow(int(digit), degree) for digit in str(number))


def solution():
    return sum(i for i in range(1000, 6*(9)**5) if sum_digit_power(i, 5) == i)


if __name__ == "__main__":
    import cProfile
    with cProfile.Profile() as p:
        print(solution())
    p.print_stats()