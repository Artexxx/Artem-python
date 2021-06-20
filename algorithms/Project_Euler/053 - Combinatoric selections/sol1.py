"""
Существует ровно десять способов выбора 3 элементов из множества пяти {1, 2, 3, 4, 5}:
    123, 124, 125, 134, 135, 145, 234, 235, 245, и 345
В комбинаторике для этого используется обозначение C(5,3) = 10 число сочетаний из 5 по 3 равно 10.
В общем случае,

C(n, k) = (n!)/ (k!(n−k)!), где k ≤ n, n! = n×(n−1)×...×3×2×1 и 0! = 1.

Это значение превышает один миллион, начиная с n = 23: C(23,10) = 1144066.

Cколько значений (не обязательно различных)  C(n, k) для 1 ≤ n ≤ 100 больше одного миллиона?

    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0100898  1.009%                           4075 (Ответ)
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution():
    count = 0

    for n in range(1, 101):
        for k in range(1, n + 1):
            if combinations(n, k) > 10**6:
                count += 1
    return count


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)