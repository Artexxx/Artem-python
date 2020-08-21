"""
Найдите первые десять цифр суммы следующих ста 50-значных чисел.
    37107287533902....(num.txt)
"""


def solution(int_numbers: list) -> str:
    """Возвращает первые десять цифр суммы элементов массива.

    >>> import os
    >>> with open(os.path.dirname(__file__) + "/num.txt","r") as f:
    ...     int_numbers = [int(line) for line in f]
    >>> solution(int_numbers)
    '5537376230'
    """
    return str(sum(int_numbers))[:10]


def solution2(int_numbers: list) -> int:
    """Аналогичное решение без использования строк"""
    all_sum = sum(int_numbers)
    DIGITS_LENGTH = 10
    while all_sum >= (10 ** DIGITS_LENGTH):
        all_sum //= 10
    return all_sum

if __name__ == "__main__":
    n = int(input("Количество чисел в массиве").strip())
    int_numbers = [int(input().strip()) for _ in range(n)]
    print(solution2(int_numbers))
