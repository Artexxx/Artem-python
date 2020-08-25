# [Сумма цифр факториала](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/20.html)

>n! означает n × (n − 1) × ... × 3 × 2 × 1
>
>Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
>
>Найдите сумму цифр в числе n!.

``` python
solution   (1)  # => 1
solution   (3)  # => 6 = 6
solution   (10)  # => 27 = 3 + 6 + 2 + 8 + 8 + 0 + 0 
```

```python
from functools import reduce
solution1 = lambda n: reduce(int.__add__, map(int, str(reduce(int.__mul__, map(int, range(1, n))))))

from math import factorial
solution2 = lambda n: sum(map(int, str(factorial(n))))
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  3.32e-05   0.003%            100          648
  2  0.0006656  0.06%            1000        10539
  3  0.0412099  4.05%           10000       149346
  4  4.88259    484.14%        100000      1938780
```

## Частное решение (1)
```python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def split_and_add(number):
    sum_of_digits = 0
    while number > 0:
        last_digit = number % 10
        sum_of_digits += last_digit
        number = number // 10  # Удаление last_digit из заданного числа
    return sum_of_digits


def solution(n):
    f = factorial(n)
    result = split_and_add(f)
    return result

```
```text
  №       Время  Замедление     Число    Результат
---  ----------  ------------ -------  -----------
  1   4.24e-05   0.004%           100          648
  2   0.0029291  0.29%           1000        10539
  3   0.431312   42.84%         10000       149346
  4   7.3457     891.43%        50000       903555
```

