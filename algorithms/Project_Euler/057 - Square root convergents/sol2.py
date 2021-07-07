"""
Приближения квадратного корня
Можно убедиться в том, что квадратный корень из двух можно выразить в виде бесконечно длинной дроби.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

Приблизив это выражение для первых четырех итераций, получим:
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985, является первым случаем, в котором количество цифр в числителе превышает количество цифр в знаменателе.

У скольких дробей длина числителя больше длины знаменателя в первой тысяче приближений выражения?

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0006408  0.064%              1000          153  Ответ
  2  0.0144547  1.381%             10000         1508 <20000 function calls>
"""
from math import log10


from typing import Iterable, Tuple

def calculate_large_sum(number_strings: Iterable[str]) -> str:
    """Calculate sum of large numbers.
    Args:
        number_strings: iterable of numbers as strings to sum up.
    Returns:
        The sum of the numbers as string.
    """
    number_strings = list(number_strings)
    large_sum = ''
    new_digit = True
    digit_idx = 1
    remainder = 0
    while new_digit:
        new_digit = False
        current_sum_digit = remainder
        for number in number_strings:
            try:
                digit = int(number[-digit_idx])
                new_digit = True
            except IndexError:
                digit = 0
            current_sum_digit += digit
        large_sum = str(current_sum_digit % 10) + large_sum
        remainder = current_sum_digit // 10
        digit_idx += 1
    if remainder:
        large_sum = str(remainder) + large_sum

    return large_sum.lstrip('0') or '0'

def _multiply_large_number_and_digit(number: str, digit: int) -> str:
    """Multiply a large number (as string) and a digit."""
    large_product = ''
    remainder = 0
    for num_digit in reversed(number):
        current_product_digit = remainder + int(num_digit) * digit
        large_product = str(current_product_digit % 10) + large_product
        remainder = current_product_digit // 10
    if remainder:
        large_product = str(remainder) + large_product
    return large_product


def calculate_large_product(number1: str, number2: str, last_n_digits_only: int = 0) -> str:
    """Multiply two large numbers given as string. The result will be a string as well."""
    number1 = number1[-last_n_digits_only:]
    number2 = number2[-last_n_digits_only:]
    partial_products = []
    for digit_idx, digit_value in enumerate(reversed(number2)):
        partial_product = _multiply_large_number_and_digit(number1, int(digit_value)) + \
            ('0' * digit_idx)
        partial_products.append(partial_product)
    return calculate_large_sum(partial_products)[-last_n_digits_only:]

def get_square_root_expansions() -> Iterable[Tuple[str, str]]:
    """Get square root expansions for `sqrt(2)` as tuples `(numerator, denominator)`."""
    previous_numerator = '1'
    previous_denominator = '1'
    numerator = '3'
    denominator = '2'
    while True:
        yield numerator, denominator
        numerator, previous_numerator = calculate_large_sum(
            [calculate_large_product(numerator, '2'), previous_numerator]
        ), numerator
        denominator, previous_denominator = calculate_large_sum(
            [calculate_large_product(denominator, '2'), previous_denominator]
        ), denominator


def count_larger_numerator_expansions(threshold: int) -> int:
    """
    Count the number of expansion fractions, where the numerator contains more digits
    than the denominator in the first `threshold` square root expansions.
    """
    square_root_expansions_iter = get_square_root_expansions()
    count = 0
    for _ in range(threshold):
        numerator, denominator = next(square_root_expansions_iter)
        if len(numerator) > len(denominator):
            count += 1
    return count


def solution(threshold) -> None:
    """Main function."""
    count = count_larger_numerator_expansions(threshold)
    print(f'In the first {threshold:,} expansions, {count:,} fractions contain ' \
          f'a numerator with more digits than the denominator.')

if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile;import cProfile
    TimeProfile(solution, [1000, 1000])
    with cProfile.Profile() as pr:
        solution(1000)
    pr.print_stats()