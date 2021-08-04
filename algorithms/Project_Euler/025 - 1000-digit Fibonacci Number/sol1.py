"""
1000-Значное число Фибоначчи
Последовательность Фибоначчи определяется рекурсивным правилом:

        Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.

Таким образом, первые 12 членов последовательности равны:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

Двенадцатый член F12 - первый член последовательности, который содержит три цифры.

Каков индекс первого члена в последовательности Фибоначчи, который содержит n цифр?

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  1.35e-05   0.001%                10           45
  2  0.0001689  0.016%               100          476
  3  0.0281723  2.800%              1000         4782 <Ответ>
"""
import itertools


def solution(N):
    """Возвращает индекс первого члена в последовательности Фибоначчи, который должен содержать n цифр.

    >>> solution(1000)
    4782
    >>> solution(100)
    476
    >>> solution(50)
    237
    >>> solution(3)
    12
    """
    prev, cur = 0, 1
    for index in itertools.count(start=1):
        if len(str(cur)) == N: return index
        ### prev = fibonacci(i - 1), cur = fibonacci(i) ###
        prev, cur = cur, prev + cur




if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import TimeProfile
    # TimeProfile(solution, [10, 100, 1000])
