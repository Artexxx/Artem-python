"""
Любой квадратный корень является периодическим, если записать его в виде непрерывных дробей в следующей форме:

    √N = a0 +  1
             ───────────────
             a1 +  1
                ────────────
                 a2 +  1
                    ────────
                    a3 + ...

К примеру, рассмотрим √23:

    √23 = 4 + √23 — 4 = 4 +   1   = 4 +   1
                           ────────    ──────────────
                           1/√23—4     1 + (√23 – 3)/7

Продолжив это преобразование, мы получим следующее приближение:

    √23 = 4 +  1
             ────────────────
             1 +   1
                ─────────────
                3 +  1
                   ──────────
                   1 +  1
                      ───────
                      8 + ...

Этот процесс можно обобщить в следующем виде:

    a0 = 4, 1 / (√23—4) = (√23+4) / 7 = 1 + (√23—3) / 7
    a1 = 1, 7 / (√23—3) = (7(√23+3)) / 14 = 3 + (√23—3) / 2
    a2 = 3, 2 / (√23—3) = (2(√23+3)) / 14 = 1 + (√23—4) / 7
    a3 = 1, 7 / (√23—4) = (7(√23+4)) / 7 = 8 + √23—4
    a4 = 8, 1 / (√23—4) = (√23+4) / 7 = 1 + √23—3 7
    a5 = 1, 7 / (√23—3) = (7(√23+3)) / 14 = 3 + (√23—3) / 2
    a6 = 3, 2 / (√23—3) = (2(√23+3)) / 14 = 1 + (√23—4) / 7
    a7 = 1, 7 / (√23—4) = (7(√23+4)) / 7 = 8 + √23—4

Нетрудно заметить, что последовательность является периодической. Для краткости введем обозначение √23 = [4;(1,3,1,8)], чтобы показать что блок (1,3,1,8) бесконечно повторяется.

Первые десять представлений непрерывных дробей (иррациональных) квадратных корней:

    √2 = [1;(2)], период = 1
    √3 = [1;(1,2)], период = 2
    √5 = [2;(4)], период = 1
    √6 = [2;(2,4)], период = 2
    √7 = [2;(1,1,1,4)], период = 4
    √8 = [2;(1,4)], период = 2
    √10 = [3;(6)], период = 1
    √11 = [3;(3,6)], период = 2
    √12 =  [3;(2,6)], период = 2
    √13 = [3;(1,1,1,1,6)], период = 5

Период является нечетным у ровно четырех непрерывных дробей при N ≤ 13.

У скольких непрерывных дробей период является нечетным при N ≤ 10000?

  №     Время  Замедление      Аргумент    Результат
---  --------  ------------  ----------  -----------
  1  0.146717  14.672%            10000         1322 (Ответ)
  2  3.93768   379.097%          100000        11486
"""
from collections import namedtuple
from math import sqrt

ContinuedFraction = namedtuple('ContinuedFraction', 'integer coefficients base')


def find_continuted_fraction(number):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion"""

    if int(sqrt(number)) == sqrt(number):
        return ContinuedFraction(int(sqrt(number)), (), number)

    numerator = 0.0
    denominator = 1.0
    root = int(sqrt(number))
    coefficients = [root]

    while coefficients[-1] != 2 * root:
        numerator = denominator * coefficients[-1] - numerator
        denominator = (number - numerator ** 2) / denominator
        next_coefficient = int((root + numerator) / denominator)
        coefficients.append(next_coefficient)

    return ContinuedFraction(root, coefficients[1:], number)


def solution(LIMIT):
    """
    Находит количество непрерывных дробей период является нечетным при N ≤ 10000.
    """
    result_count = 0

    for n in range(2, LIMIT + 1):
        fraction = find_continuted_fraction(n)
        if len(fraction.coefficients) % 2 != 0:
            result_count += 1
    return result_count


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile;
    TimeProfile(solution, [10_000, 100_000])
