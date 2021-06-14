# [Дружественные числа](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/21.html)

> Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
> Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
> а каждое из чисел a и b - дружественным числом.
>
> Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
> поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
>
> Подсчитайте сумму всех дружественных чисел меньше 10000.

``` python
solution   (50)  # => 0
solution   (100)  # => 0
solution   (1000)  # => 504
solution   (10000)  # => 31626

```

## Частное решение (1)
```python

def sum_of_divisors(n):
    total = 0
    for i in range(1, int(sqrt(n) + 1)):
        if (n % i) == 0:
            total += i + (n // i)
    return total - n

def solution(LIMIT):
    total = 0
    for m in range(2, LIMIT):
        n = sum_of_divisors(m)

        # M и N удовлетворяют условиям дружественных пар:  m < n < LIMIT
        if (m < n < LIMIT) and sum_of_divisors(n) == m:
            total += m + n
    return total

```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0001212  0.012%            100            0
  2  0.0020599  0.19%            1000          504
  3  0.047425   4.54%           10 000        31626
  4  1.20486    115.74%        100 000       852810
```

## Частное решение (2)

```python
def solution(LIMIT):
    # Находим сумму собственных делителей для каждого числа
    sum_of_divisors = [0] * LIMIT
    for i in range(1, len(sum_of_divisors)):
        for j in range(i * 2, len(sum_of_divisors), i):
            sum_of_divisors[j] += i

    # Находим все дружественные пары в пределах досягаемости
    total = 0
    for i in range(1, len(sum_of_divisors)):
        j = sum_of_divisors[i]
        if j != i and j < LIMIT and sum_of_divisors[j] == i:
            total += i
    return total
```
```text
 №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  5.66e-05   0.006%           100             0
  2  0.0007475  0.07%            1000          504
  3  0.0100173  0.93%           10 000        31626
  4  0.126762   11.67%         100 000       852810
  5  2.08884    196.21%       1 000 000     25275024
```