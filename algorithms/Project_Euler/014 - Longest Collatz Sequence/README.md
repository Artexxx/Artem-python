# [Самая длинная последовательность Коллатца](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/14.html)

>Следующая повторяющаяся последовательность определена для множества натуральных чисел:
>
>n → n/2 (n - четное)
>n → 3n + 1 (n - нечетное)
>
>Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
>
>13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
>
>Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
>
> Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.
>
>Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
>
>Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.

``` python
solution   (10000) # =>   6171 = counter: 262
solution  (100000) # =>  77031 = counter: 351
solution (1000000) # => 837799 = counter: 525
```

## Частное решение (1)

```python
def solution(n):
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
```
```text
  №       Время  Замедление      Число  Результат
---  ----------  ------------  -------  ------------------------------------------
  1   0.0121054  1.211%           1000  {'counter': 179, 'largest_number': 871}
  2   0.159858   14.78%          10000  {'counter': 262, 'largest_number': 6171}
  3   1.9221     176.22%        100000  {'counter': 351, 'largest_number': 77031}
  4  10.7897     886.76%        500000  {'counter': 449, 'largest_number': 410011}
```

## Частное решение (2)

[+] кэшируем значение для всех целочисленных аргументов, чтобы ускорить вычисление

```python
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
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.001678   0.168%           1000          871
  2  0.0132201  1.15%           10000         6171
  3  0.147351   13.41%         100000        77031
  4  1.49403    134.67%       1000000       837799
```

## Частное решение (2-Opt)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def collatz_chain_length(x):
    if x == 1: return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return collatz_chain_length(y) + 1  

def solution(n):
    return max(range(1, n), key=collatz_chain_length)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.000873   0.087%           1000          871
  2  0.0066451  0.58%           10000         6171
  3  0.0803638  7.37%          100000        77031
  4  0.882243   80.19%        1000000       837799
```