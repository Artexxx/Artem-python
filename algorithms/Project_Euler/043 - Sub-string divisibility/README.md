# [Делимость подстрок](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/43.html)


>Число 1406357289, является пан-цифровым, поскольку оно состоит из цифр от 0 до 9 в определенном порядке. Помимо этого, оно также обладает интересным свойством делимости подстрок.
>
>Пусть d(1) будет 1-ой цифрой, d(2) будет 2-ой цифрой, и т.д. В таком случае, можно заметить следующее:
>
> ```
> d(2)d(3)d(4) = 406 делится на 2 без остатка
> d(3)d(4)d(5) = 063 делится на 3 без остатка
> d(4)d(5)d(6) = 635 делится на 5 без остатка
> d(5)d(6)d(7) = 357 делится на 7 без остатка
> d(6)d(7)d(8) = 572 делится на 11 без остатка
> d(7)d(8)d(9) = 728 делится на 13 без остатка
> d(8)d(9)d(10) = 289 делится на 17 без остатка
>```
>
>Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих данным свойством.

``` python
solution  () => 16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
```

## Частное решение (1)

```python
import itertools


def has_substring_divisibility(n: str):
    substring_divisors = {
        (2, 4): 2,
        (3, 5): 3,
        (4, 6): 5,
        (5, 7): 7,
        (6, 8): 11,
        (7, 9): 13,
        (8, 10): 17
    }
    for t, d in substring_divisors.items():
        if int(n[t[0] - 1:t[1]]) % d:
            return False
    return True


def find_substring_divisible_pandigitals():
    pandigital_numbers = [''.join(p) for p in list(itertools.permutations('0123456789')) if p[0] != '0']
    pandigital_numbers_with_substring_divisibility = filter(has_substring_divisibility, pandigital_numbers)
    return pandigital_numbers_with_substring_divisibility


def solution():
    """
    Возращает сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих свойством - делимость подстрок
    >>> solution()
    ... 16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
    """
    return sum(map(int, find_substring_divisible_pandigitals()))

```
```
  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
 1   4.01282   401.282%        None  16695334890
```

## Нормальное решение (1)
```python
from itertools import product


def distinct_digits(iterable):
    return filter(lambda s: len(frozenset(s)) == len(s), iterable)


def three_digit_multiples(p):
    return map(lambda n: str(n).zfill(3), range(p, 1000, p))


def two_digit_overlaps(heads, tails):
    for head, tail in product(heads, tails):
        if head[-2:] == tail[:2]:
            yield head + tail[2:]


def substring_divisible_pandigitals():
    tails = distinct_digits(three_digit_multiples(17))
    for p in [13, 11, 7, 5, 3, 2, 1]:
        heads = distinct_digits(three_digit_multiples(p))
        tails = distinct_digits(two_digit_overlaps(heads, tails))
    return tails


def solution():
    """
    Возращает сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих свойством - делимость подстрок
    >>> solution()
    ... 16695334890 # sum{1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289}
    """
    return sum(map(int, substring_divisible_pandigitals()))
```
```
  №      Время  Замедление    Число      Результат
---  ---------  ------------  -------  -----------
  1  0.0050144  0.501%                 16695334890
```