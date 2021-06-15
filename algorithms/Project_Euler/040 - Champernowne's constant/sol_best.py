"""
Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:

0.12345678910{1}112131415161718192021...

Видно, что 12-ая цифра дробной части - 1.

Также дано, что d_n представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

# количество цифр каждой серии: 9, 180, 2700, ..., 9·x·10^(x−1)
ch_digits_count = [9 * (x + 1) * 10 ** x for x in range(20)]


def get_digit(indicies):
    '''Возразает цифру в позиции indicies из постоянной Чамперноуна'''
    i = 0
    while indicies > ch_digits_count[i]:
        indicies -= ch_digits_count[i]
        i += 1
    L, d = divmod((indicies - 1), i + 1)
    return int(str(10 ** i + L)[d])


def solution():
    """
    >>> solution()
    210 # =>   PROD{1, 5, 3, 7, 2, 1, 210}
    """
    result_product = 1
    for power in range(2, 7):
        ch_digit = get_digit(10 ** power)
        result_product *= ch_digit
    return result_product


if __name__ == '__main__':
    print(solution())
