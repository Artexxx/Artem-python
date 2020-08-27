def binarysearch(mylist, items):
    """ Возращает индекс числа items в списке mylist.
    Сложность: lg n

    [-] список жолжен быть отсортирован (Сложномть сортировки: n lg n )

    >>> binarysearch([1, 2, 4, 5, 6, 9], 6)
    ... 4
    """
    start = 0
    stop = len(mylist)
    while start <= stop:
        mid = (start + stop) // 2
        dogadka = mylist[mid]
        if dogadka > items:
            stop = mid - 1
        elif dogadka < items:
            start = mid + 1
        else:
            return mid


if __name__ == '__main__':
    print("App Binary search -> index =", binarysearch([1, 2, 4, 5, 6, 9], 6))
    print('index =', binarysearch(["john", "mark", "ronald", "sarah"], "sarah"))
