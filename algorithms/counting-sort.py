"""
Алгоритм сортировки подсчетом:
    Подсчитываем, сколько раз в массиве встречается каждое значение,
    и заполняем массив подсчитанными элементами в соответствующих количествах.

Сложность сортировки по времени
    Худшая O(n + k)
    Средняя O(n + k)
    Лучшая O(n)
"""


def SimpleCountingSort(alist):
    largest = max(alist)
    counter = [0] * (largest + 1)
    for x in alist:
        counter[x] += 1
    alist[:] = []
    for number in range(largest):
        alist += [number] * counter[number]
    return alist


if __name__ == '__main__':
    arr = [15, 5, 50, 10, 20, 25, 20]
    print(SimpleCountingSort(arr))
