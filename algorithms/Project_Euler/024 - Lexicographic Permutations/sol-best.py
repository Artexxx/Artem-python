"""
Перестановка - это упорядоченная выборка объектов.
К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4.
 Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем называть словарным.
  Словарные перестановки из цифр 0, 1 и 2 представлены ниже:

    012   021   102   120   201   210

Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
"""
from math import factorial


def solution(POS) -> int:
    """Возращает миллионную словарнаю перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9.

     >>> solution()
     2_783_915_460
     """
    # Индекс позиции - это как в списке. N-й элемент - это элемент с индексом n-1
    pos = POS - 1

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # определется каждая цифра N-й лексикографической перестановки
    digit_count = len(digits)
    permutation_digits = []
    # for i in range(digit_count, 0, -1):
    for i in range(1, digit_count):
        digit, pos = divmod(pos, factorial(digit_count - i))
        permutation_digits.append(digits[digit])
        print(digits)
        del digits[digit]

    # добавляется оставшаяся цифра
    permutation_digits.append(digits[0])
    return int(''.join(permutation_digits))


def solution_1(POS):
    """ Аналогичное решение """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    permutation_digits = []

    # Индекс позиции - это как в списке. N-й элемент - это элемент с индексом n-1
    pos = POS - 1
    for i in reversed(range(len(digits))):
        c = pos // factorial(i)  # math.floor
        permutation_digits.append(digits[c])
        digits.remove(digits[c])
        pos = pos - c * factorial(i)
    return permutation_digits


if __name__ == "__main__":
    print(solution_1(10 ** 6))
