"""
Факториалы цифр
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""
from itertools import combinations_with_replacement

factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

def solution():
    """
    Возвращает сумму всех чисел, равных сумме факториалов своих цифр.

    >>> solution()
    40730
    """
    result = 0
    for i in [2, 3, 4, 5, 6, 7]:
        for number in combinations_with_replacement(range(10), i):
            candidate = sum(factorials[i] for i in number)
            if sorted(map(int, str(candidate))) == sorted(number):
                result += candidate
    return result


if __name__ == '__main__':
    print(solution())
