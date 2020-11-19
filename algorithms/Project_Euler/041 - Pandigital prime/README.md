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

def is_pandigital_prime(n: int, n_is_prime: bool) -> bool:
    if n_is_prime:
        str_n = str(n)
        n_is_pandigital = set(str_n) == set('7654321') and len(str_n) == 7
        return n_is_pandigital
    return False


def solution():
    """
    Возращает нибольшее n-значное пан-цифровое простое число
    >>> solution()
    ... 7652413
    """
    limit = 7654321+1
    sieve_bit_array = bit_sieve(limit)
    return max(n for n in range(3, limit) if is_pandigital_prime(n, sieve_bit_array[n]))
```