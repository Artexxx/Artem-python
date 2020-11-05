"""
Целые прямоугольные треугольники
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
"""


def solution(LIMIT=1000):
    """
    Возращает периметр, для которого существует максимальное число решений
    >>> solution()
    ... 840 # 9 решений
    """
    result_perimeter = None
    max_count = 0

    for p in range(2, LIMIT, 2):
        count_solutions = 0
        for a in range(2, int(p / 3)):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                count_solutions += 1
        if count_solutions > max_count:
            max_count = count_solutions
            result_perimeter = p
    return result_perimeter


if __name__ == '__main__':
    print(solution())
