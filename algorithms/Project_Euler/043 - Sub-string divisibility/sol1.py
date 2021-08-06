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
import itertools


def has_substring_divisibility(n: str):
    substring_divisors = {
        (2, 4): 2,
        (3, 5): 3,
        (4, 6): 5,
        (5, 7): 7,
        (6, 8): 11,
        (7, 9): 13,
        (8, 10): 17
    }
    for t, d in substring_divisors.items():
        if int(n[t[0] - 1:t[1]]) % d:
            return False
    return True


def find_substring_divisible_pandigitals():
    pandigital_numbers = (''.join(p) for p in list(itertools.permutations('0123456789')) if p[0] != '0')
    pandigital_numbers_with_substring_divisibility = filter(has_substring_divisibility, pandigital_numbers)
    return pandigital_numbers_with_substring_divisibility


def solution():
    """
    Возвращает сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих свойством - делимость подстрок
    >>> solution()
    16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
    """
    return sum(map(int, find_substring_divisible_pandigitals()))


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import my_time_this
    my_time_this(solution, [])
