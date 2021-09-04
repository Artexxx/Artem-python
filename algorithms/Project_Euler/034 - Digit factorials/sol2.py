"""
Факториалы цифр
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""
from itertools import combinations_with_replacement


def solution():
    """
    Возвращает сумму всех чисел, равных сумме факториалов своих цифр.

    >>> solution()
    40730
    """
    factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    digits = range(10)
    lengths = [2, 3, 4, 5, 6, 7]
    result_sum = 0
    for lenght in lengths:
        for number in combinations_with_replacement(digits, lenght):
            candidate = sum(factorials[d] for d in number)
            if sorted(map(int, str(candidate))) == sorted(number):
                result_sum += candidate
    return result_sum


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.3}ms".format(default_timer() - start_time))
