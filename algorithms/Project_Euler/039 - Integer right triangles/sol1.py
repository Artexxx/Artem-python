"""
Целые прямоугольные треугольники
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
"""
from itertools import product
from math import sqrt

is_valid_sqrt = lambda n: n == int(n)
is_valid_triangle = lambda a, b, c: all((a, b, c))


def perimeters_generator():
    for a, b in product(range(500), range(500)):
        c: float = sqrt(a * a + b * b)
        if is_valid_sqrt(c) and a + b + c <= 1000 and is_valid_triangle(a, b, c):
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
    count_dict = dict()
    for p in perimeters_generator():
        if count_dict.get(p):
            count_dict[p] += 1
        else:
            count_dict[p] = 1
    return max(count_dict, key=lambda x: count_dict[x])


if __name__ == '__main__':
    print(solution())
