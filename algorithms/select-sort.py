"""
Алгоритм сортировки выбором:
  1. В неотсортированном подмассиве ищется локальный максимум (минимум)
  2. Найденный максимум (минимум) меняется местами с последним (первым) элементом в подмассиве
  3. Если в массиве остались неотсортированные подмассивы — повтори пункт 1

Сложность сортировки по времени
    Худшая  O(n^2)
    Средняя O(n^2)
    Лучшая  O(n^2)
"""


def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
    return alist

if __name__ == '__main__':
    arr = [15, 5, 50, 10, 20, 25, 20]
    print(selection_sort(arr))
