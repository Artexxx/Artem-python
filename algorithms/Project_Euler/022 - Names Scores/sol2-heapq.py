"""
Используя массив имён, содержащий более пяти тысяч имен, начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке.
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
"""
import os, heapq


def letter_index_upper(letter) -> int:
    """Возвращает алфавитный индекс заглавной буквы.
    Например: 'A' -> 1, 'Z' -> 26.
    """
    return ord(letter) - ord('A') + 1


def name_score(name, position) -> int:
    """Возвращает оценку для имени в позиции при сортировке в алфавитном порядке.
    """
    score = sum(map(letter_index_upper, name))
    return position * score


def solution() -> int:
    """Возращает сумму очков имен в файле `p022_names.txt`.

    >>> solution()
    871198282
    """
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = str(file.readlines()[0]).split(",")
    heapq.heapify(names)  # сортировка

    total = 0
    for i in range(1, len(names) + 1):
        # heappop - возращает min элемент, удаляет его из кучи
        total += name_score(heapq.heappop(names), i)
    return total


if __name__ == "__main__":
    print(solution())
