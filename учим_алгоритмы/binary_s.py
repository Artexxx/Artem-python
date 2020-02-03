def binarysearch(mylist, items):
    """ вводите список чисел(mylist) и число(items} которое хотите найти """
    start = 0
    stop = len(mylist) - 1
    while start <= stop:
        mid = (start + stop) / 2
        dogadka = list(mid)
        if dogadka == items:
            return mid
        if dogadka > items:
            stop = mid - 1
        else:
            stop = mid + 1
    return None


mylist = [1, 2, 4, 5, 6, 9]

print(binarysearch(mylist, 4))
