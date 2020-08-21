"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:
    n → n/2 (n - четное)
    n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

  №       Время  Замедление      Число  Результат
---  ----------  ------------  -------  ------------------------------------------
  1   0.0121054  1.211%           1000  {'counter': 179, 'largest_number': 871}
  2   0.159858   14.78%          10000  {'counter': 262, 'largest_number': 6171}
  3   1.9221     176.22%        100000  {'counter': 351, 'largest_number': 77031}
  4  10.7897     886.76%        500000  {'counter': 449, 'largest_number': 410011}
"""


def solution(n):
    """Возвращает число меньше n, которое генерирует самую длинную последовательность Коллатца

    n → n/2 (n - четное)
    n → 3n + 1 (n - нечетное)

    [-] >>> solution(1000000)
    [-] {'counter': 525, 'largest_number': 837799}
    >>> solution(200)
    {'counter': 125, 'largest_number': 171}
    >>> solution(5000)
    {'counter': 238, 'largest_number': 3711}
    >>> solution(15000)
    {'counter': 276, 'largest_number': 13255}
    """
    largest_number = 0
    pre_counter = 0

    for input1 in range(n):
        counter = 1
        number = input1

        while number > 1:
            if number % 2 == 0:
                number /= 2
                counter += 1
            else:
                number = (3 * number) + 1
                counter += 1

        if counter > pre_counter:
            largest_number = input1
            pre_counter = counter
    return {"counter": pre_counter, "largest_number": largest_number}


if __name__ == "__main__":
    result = solution(int(input().strip()))
    print(("Largest Number:", result["largest_number"], "->", result["counter"], "digits"))
    ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [1000, 10_000, 100_000, 500_000])