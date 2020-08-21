from typing import List


def compute_digit_and_carry(digits):
    """
    >>> compute_digit_and_carry([120, 7])
    digit, carry = (7, 12)
    """
    s = sum(digits)
    return s % 10, s // 10


def get_numbers_digit(numbers, ith):
    """
    >>> get_numbers_digit([[1, 2, 3],
    ...                    [4, 5, 6],
    ...                    [7, 8, 9]], 0)
    digits = [1, 4, 7]
    """
    return [int(r[ith]) for r in numbers]


def solve(numbers: List[str], first_n_digits) -> str:
    """Возвращает первые десять цифр суммы элементов массива.
   >>> import os
   >>> with open(os.path.dirname(__file__) + "/num.txt","r") as f:
   ...     numbers = [line for line in f]
   >>> solution(numbers, first_n_digits=10)
   '5537376230'
    """

    digit_number = len(numbers[0])
    carry = 0
    digits = []
    for c in range(digit_number - 1, -1, -1):
        d, carry = compute_digit_and_carry(get_numbers_digit(numbers, c) + [carry])
        digits.insert(0, d)
    digits = list(str(carry)) + digits
    return ''.join(map(str, digits[:first_n_digits]))


print(solve(numbers=['786', '457'], first_n_digits=4))
