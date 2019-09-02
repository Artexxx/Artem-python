"""сортировка выбором"""


def random_list(N: int = 124, n: int = 1, b: int = 99) -> list:
    """заполняем список (a) длиной (N) рандомными числами в диапозоне от(n=1 до b=99)"""
    from random import randint
    a = []
    for i in range(N):
        a.append(randint(n, b))
    return (a)


def find_min(arr):
    """ищет минимальный элемент списка(arr)"""
    min = arr[0]
    fin_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            fin_index = i
    return fin_index


def select_sort(arr: list = random_list()) -> list:
    """сортирует выбором  /по возростанию/ список(arr) в список (NewArr)"""
    NewArr = []
    for i in range(len(arr)):
        min = find_min(arr)
        NewArr.append(arr.pop(min))
    return NewArr


print(random_list(10,1,9999))
print(select_sort())
