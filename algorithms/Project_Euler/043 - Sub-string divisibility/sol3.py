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

    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0008629  0.086%                    16695334890
"""


def convert_to_number(*digits):
    """ Соединяет цифры в число
    >>> convert_to_number(1,2,3)
    123
    """
    number = 0
    for d in digits:
        number *= 10
        number += d
    return number


def solution():
    """
    Возвращает сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих свойством - делимость подстрок
    >>> solution()
    16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
    """
    return sum(
        convert_to_number(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
        for d10 in set(range(10))
        for d9 in set(range(10)) - {d10}
        for d8 in set(range(10)) - {d10, d9}
        if convert_to_number(d8, d9, d10) % 17 == 0
        for d7 in set(range(10)) - {d10, d9, d8}
        if convert_to_number(d7, d8, d9) % 13 == 0
        for d6 in set(range(10)) - {d10, d9, d8, d7}
        if convert_to_number(d6, d7, d8) % 11 == 0
        for d5 in set(range(10)) - {d10, d9, d8, d7, d6}
        if convert_to_number(d5, d6, d7) % 7 == 0
        for d4 in set(range(10)) - {d10, d9, d8, d7, d6, d5}
        if convert_to_number(d4, d5, d6) % 5 == 0
        for d3 in set(range(10)) - {d10, d9, d8, d7, d6, d5, d4}
        if convert_to_number(d3, d4, d5) % 3 == 0
        for d2 in set(range(10)) - {d10, d9, d8, d7, d6, d5, d4, d3}
        if convert_to_number(d2, d3, d4) % 2 == 0
        for d1 in set(range(10)) - {d10, d9, d8, d7, d6, d5, d4, d3, d2}
    )


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;

    sys.path.append('..')
    from time_profile import TimeProfile

    TimeProfile(solution)
