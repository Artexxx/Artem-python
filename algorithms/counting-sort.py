"""
Алгоритм сортировки подсчетом:
    Подсчитываем, сколько раз в массиве встречается каждое значение,
    и заполняем массив подсчитанными элементами в соответствующих количествах.

Сложность сортировки по времени
    Худшая O(n + k)
    Средняя O(n + k)
    Лучшая O(n)
"""


def simple_counting_sort(array):
    largest = max(array)
    counter = [0] * (largest + 1)
    for x in array:
        counter[x] += 1
    array[:] = []
    for number in range(largest):
        array += [number] * counter[number]
    return array


if __name__ == '__main__':
    array = [15, 5, 50, 10, 20, 25, 20]
    print(simple_counting_sort(array))
