"""
Используя массив имён, содержащий более пяти тысяч имен, начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке.
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
"""
import os


def solution():
    """Возвращает сумму очков имен в файле `p022_names.txt`.

    >>> solution()
    871198282
    """
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = file.readline().split(",")
        names.sort()
    name_score = 0
    total_score = 0
    for i, name in enumerate(names):
        for letter in name:
            name_score += ord(letter) - 64

        total_score += (i + 1) * name_score
        name_score = 0
    return total_score


if __name__ == "__main__":
    print(solution())
