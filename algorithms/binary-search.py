def binary_search(list_, item):
    """ Возращает индекс числа item в списке list_.
    Сложность: lg n

    [-] список должен быть отсортирован, cложномть сортировки: n lg n

    >>> binary_search([1, 2, 4, 5, 6, 9], 6)
    ... 4
    """
    start = 0
    stop = len(list_)

    while start <= stop:
        mid = (start + stop) // 2
        target = list_[mid]

        if target > item:
            stop = mid - 1
        elif target < item:
            start = mid + 1
        else:
            return mid
    return -1


def binary_search_recursive(list_, start, stop, item):
    """ Возращает индекс числа item в списке list_.
    Сложность: lg n

    [-] список должен быть отсортирован, cложномть сортировки: n lg n

    >>> list_names = ["john", "mark", "ronald", "sarah"]
    >>> start, stop = 0, len(list_names)
    >>> binary_search_recursive(list_names, start, stop, "sarah")
    ... 4
    """

    while start <= stop:
        mid = (start + stop) // 2
        target = list_[mid]

        if target > item:
            return binary_search_recursive(list_, start, mid - 1, item)
        elif target < item:
            return binary_search_recursive(list_, mid + 1, stop, item)
        else:
            return mid
    return -1


if __name__ == '__main__':
    print("App Binary search -> index =", binary_search([1, 2, 4, 5, 6, 9], 6))
    print('index =', binary_search(["john", "mark", "ronald", "sarah"], "sarah"))

    list_names = ["john", "mark", "ronald", "sarah"]
    start, stop = 0, len(list_names)
    print('index =', binary_search_recursive(list_names, start, stop, "sarah"))
