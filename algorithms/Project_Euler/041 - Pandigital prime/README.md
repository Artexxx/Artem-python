# [Пан-цифровое простое число](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/41.html)

>Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз. 
>
>К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.
>
>Какое существует наибольшее n-значное пан-цифровое простое число?


``` python
solution  () => 7652413
```

## Частное решение (1)

_Анализ:_ 9 и 8-значные пан-цифровые числа делятся на 3 и поэтому не могут быть простыми.

```python
def permutations(lst):
    if len(lst) == 0: yield []
    elif len(lst) == 1: yield lst
    for i in range(len(lst)):
        x = lst[i]
        xs = lst[:i] + lst[i + 1:]
        for p in permutations(xs):
            yield [x] + p


def solution():
    """
    Возращает нибольшее n-значное пан-цифровое простое число
    >>> solution()
    ... 7652413
    """
    for perm_lst in permutations(list('7654321')):
        pandigital = int(''.join(perm_lst))
        if is_prime(pandigital):
            return pandigital
```