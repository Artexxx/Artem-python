"""
Целые прямоугольные треугольники
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
"""
from collections import defaultdict
from math import sqrt

is_valid_sqrt = lambda n: n == int(n)


def perimeters_generator():
    for a in range(1, 1000 // 3):  # Нужно место для b и c
        for b in range(a + 1, 1000 - (2 * a)):  # Нужно место для c
            c: float = sqrt(a * a + b * b)
            if a + b + c > 1000:
                break
            if is_valid_sqrt(c):
                yield a + b + int(c)


def solution():
    """
    Возвращает периметр, для которого существует максимальное число решений
    >>> solution()
    840 # 16 решений
    Полученные решения:
     [40, 399, 401]
     [40, 399, 401]
     [56, 390, 394]
     [56, 390, 394]
          ...
     [210, 280, 350]
     [210, 280, 350]
     [240, 252, 348]
     [240, 252, 348]
    """
    count_dict = defaultdict(int)
    for p in perimeters_generator():
        count_dict[p] += 1
    return max(count_dict, key=lambda x: count_dict[x])


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.5}ms".format(default_timer() - start_time))
