"""
Делимость подстрок
Число 1406357289, является пан-цифровым, поскольку оно состоит из цифр от 0 до 9 в определенном порядке.
Помимо этого, оно также обладает интересным свойством делимости подстрок.

Пусть d1 будет 1-ой цифрой, d2 будет 2-ой цифрой, и т.д. В таком случае, можно заметить следующее:

d2d3d4=406 делится на 2 без остатка
d3d4d5=063 делится на 3 без остатка
d4d5d6=635 делится на 5 без остатка
d5d6d7=357 делится на 7 без остатка
d6d7d8=572 делится на 11 без остатка
d7d8d9=728 делится на 13 без остатка
d8d9d10=289 делится на 17 без остатка
Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих данным свойством.

  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
 1   4.01282   401.282%        None  16695334890
"""

from itertools import product


def distinct_digits(iterable):
    return filter(lambda s: len(frozenset(s)) == len(s), iterable)


def three_digit_multiples(p):
    return map(lambda n: str(n).zfill(3), range(p, 1000, p))


def two_digit_overlaps(heads, tails):
    for head, tail in product(heads, tails):
        if head[-2:] == tail[:2]:
            yield head + tail[2:]


def substring_divisible_pandigitals():
    tails = distinct_digits(three_digit_multiples(17))
    for p in [13, 11, 7, 5, 3, 2, 1]:
        heads = distinct_digits(three_digit_multiples(p))
        tails = distinct_digits(two_digit_overlaps(heads, tails))
    return tails


def solution():
    """
    Возращает сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих свойством - делимость подстрок
    >>> solution()
    ... 16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
    """
    return sum(map(int, substring_divisible_pandigitals()))


if __name__ == '__main__':

    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import my_time_this
    my_time_this(solution, [])
