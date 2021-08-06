"""
Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
1 = 1^4 не считается, так как это - не сумма.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.

# Result: 443839
# Profile: 2_834_486 function calls (2_540_240 primitive calls) in 0.921 seconds

"""
from functools import lru_cache
from typing import Any, Callable, Union


@lru_cache(maxsize=10)
def pow_(a, b, /):
    return pow(a, b)


def sum_digit_power(number, degree) -> int:
    """
    Возвращает сумму цифр числа `number`, которые были возведены в степень `degree`

    >>> sum_digit_power(4151, 5)
    4151 #=> sum(1024, 1, 3125, 1)
    """
    return sum(pow_(int(digit), degree) for digit in str(number))


def solution():
    """
    >>> solution(5)
    443839
    """
    is_pownumber = lambda x: sum_digit_power(x, 5) == x
    return sum(filter(is_pownumber, range(1000, (9 ** 5) * 5 + 1)))


if __name__ == "__main__":
    import cProfile

    with cProfile.Profile() as p:
        print(solution())
    p.print_stats()
