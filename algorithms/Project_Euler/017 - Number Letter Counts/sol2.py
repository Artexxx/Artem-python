"""
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?

Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского
английского.
"""


def solution(n):
    """Возвращает количество букв, используемых для записи всех чисел от 1 до n.
    [*] где n меньше или равно 1000.

    >>> solution(1000)
    21124
    >>> solution(5)
    19
    """
    # zero, one, two, ..., nineteen
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # twenty, thirty, ..., ninety
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    count = 0
    for i in range(1, n + 1):
        if i < 1000:
            if i >= 100:
                # add number of letters for "n hundred"
                count += ones_counts[i // 100] + 7

                if i % 100 != 0:
                    # add number of letters for "and" if number is not multiple of 100
                    count += 3

            if 0 < i % 100 < 20:
                # add number of letters for one, two, three, ..., nineteen
                # (could be combined with below if not for inconsistency in teens)
                count += ones_counts[i % 100]
            else:
                # add number of letters for twenty, twenty one, ..., ninety nine
                count += ones_counts[i % 10]
                count += tens_counts[(i % 100 - i % 10) // 10]
        else:
            count += ones_counts[i // 1000] + 8
    return count


if __name__ == "__main__":
    print(solution(int(input().strip())))
