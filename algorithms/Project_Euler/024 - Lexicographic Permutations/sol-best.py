"""
Перестановка - это упорядоченная выборка объектов.
К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4.
 Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем называть словарным.
  Словарные перестановки из цифр 0, 1 и 2 представлены ниже:

    012   021   102   120   201   210

Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
"""
from math import factorial


def solution(position=10**6):
    """Возвращает N словарнаю перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9.

     >>> solution()
     2_783_915_460
     """
    digits = list('0123456789')
    digit_count = len(digits)
    result_digits_sequence = []

    # Определется каждая цифра N-й лексикографической перестановки
    for index in range(1, digit_count):
        idx_digit, position = divmod(position, factorial(digit_count-index))
        result_digits_sequence.append(digits[idx_digit])
        print(*digits)
        del digits[idx_digit]

    # Добавляется оставшаяся цифра
    result_digits_sequence.append(digits[0])
    return int(''.join(result_digits_sequence))


def solution2(position=10**6):
    """Старое решение

     >>> solution2()
     2_783_915_460
     """
    digits = list('0123456789')
    digit_count = len(digits)
    result_digits_sequence = []

    # Определется каждая цифра N-й лексикографической перестановки
    for index in range(1, digit_count):
        idx_digit = position // factorial(digit_count-index)
        result_digits_sequence.append(digits[idx_digit])
        print(*digits)
        del digits[idx_digit]
        position = position - idx_digit * factorial(index)

    # Добавляется оставшаяся цифра
    result_digits_sequence.append(digits[0])
    return int(''.join(result_digits_sequence))


if __name__ == "__main__":
    print(solution(10 ** 6))
