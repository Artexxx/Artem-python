"""
Используя массив имён, содержащий более пяти тысяч имен, начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке.
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?

    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0084408  0.844%                      871190344 <108414 function calls>
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
    """Возвращает сумму очков имен в файле `p022_names.txt`.

    >>> solution()
    871198282
    """
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = file.readline().split(",")
        heapq.heapify(names)  # Сортировка
    total = 0
    for i in range(1, len(names) + 1):
        # heappop - Возвращает min элемент, удаляет его из кучи
        total += name_score(heapq.heappop(names), i)
    return total


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile; import cProfile
    TimeProfile(solution)
    with cProfile.Profile() as pr:
        solution()
        print('\n\n');pr.print_stats()
