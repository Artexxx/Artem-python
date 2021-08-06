"""
Пятиугольные числа вычисляются по формуле: P_n = n(3n−1)/2. Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P_4 + P_7 = 22 + 70 = 92 = P_8. Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

Найдите пару пятиугольных чисел P_j и P_k, для которых сумма и разность являютя пятиугольными числами и значение D = |P_k − P_j| минимально, и дайте значение D в качестве ответа.

  №     Время  Замедление    Число      Результат
---  --------  ------------  -------  -----------
  1  0.234372  23.437%                    5482660 # diff{7042750, 1560090}
  2  20.12323                          8476206790 # diff{12599537925, 4123331135}

"""


def generate_polygonal(type_number):
    """Генерирует фиругные числа

    >>> generate_polygonal(type_number=3)
    1 3 6 10 15 21 28 36 ...
    >>> generate_polygonal(type_number=4)
    1 4 9 16 25 36 49 64 ...
    """
    c = type_number - 2
    a = b = 1
    while True:
        yield a
        b += c
        a += b


def generate_pentagonals_pair():
    seen = set()
    for i in generate_polygonal(type_number=5):
        for j in seen:
            p = i - j
            q = j
            if p in seen and p - q in seen:
                yield p, q
        seen.add(i)


def solution():
    """
    Возвращает разность пары пятиугольных чисел p и q, для которых сумма и разность являются пятиугольными числами.
    >>> solution()
    5482660 # diff{7042750 1560090}
    """
    p, q = next(generate_pentagonals_pair())
    return p - q


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)
