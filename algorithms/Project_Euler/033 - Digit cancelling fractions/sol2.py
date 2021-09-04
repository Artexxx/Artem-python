"""
Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать, что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.

Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.

Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат двухзначные числа как в числителе, так и в знаменателе.

Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби.
"""

from fractions import Fraction


def cancel_digit(numerator, denominator) -> Fraction:
    """
    Сокращает общую цифру в числителе и знаменателе (игнорирует 0)
    """
    if numerator % 10 == denominator // 10 and denominator % 10 != 0:
        return Fraction(numerator // 10, denominator % 10)
    elif numerator // 10 == denominator % 10 and denominator % 10 != 0:
        return Fraction(numerator % 10, denominator // 10)
    return None


def solution() -> Fraction:
    """
    Возвращает знаменатель произведения 4x особых дробей.

    >>> solution()
    100
    """
    product_fraction = Fraction(1)
    for denominator in range(12, 99):
        for numerator in range(12, denominator):
            f = Fraction(numerator, denominator)
            if cancel_digit(numerator, denominator) == f:
                product_fraction *= f
    return product_fraction.denominator


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.5}ms".format(default_timer() - start_time))