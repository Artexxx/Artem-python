"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:
    n → n/2 (n - четное)
    n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.001678   0.168%           1000          871
  2  0.0132201  1.15%           10000         6171
  3  0.147351   13.41%         100000        77031
  4  1.49403    134.67%       1000000       837799
"""

import sys


def memoize(f):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[+] F(", int(*args), ')\t => \t', dict(cache)) # TEST OUTPUT
        return cache[args]

    return wrapper


@memoize
def collatz_chain_length(x):
    if x == 1: return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return collatz_chain_length(y) + 1


def solution(n):
    """
    Возвращает число меньше n, которое генерирует самую длинную последовательность Коллатца

    n → n/2 (n - четное)
    n → 3n + 1 (n - нечетное)

    >>> solution(1000000)
    837799
    >>> solution(200)
    171
    >>> solution(5000)
    3711
    >>> solution(15000)
    13255
    """
    sys.setrecursionlimit(3000)
    return max(range(1, n), key=collatz_chain_length)


if __name__ == "__main__":
    print(solution(1_000_000))
    # ### Run Time-Profile Table ###
    # import sys;sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [1000, 10_000, 100_000, 1_000_000])
