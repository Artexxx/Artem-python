# [Круговые простые числа](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/35.html)

>Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.
>
>Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
>
>Сколько существует круговых простых чисел меньше миллиона?

``` python
solution   (10**6)  # => 55
```


## Частное решение (1)

```python
def is_circular_prime(n: int, n_is_prime: bool) -> bool:
    def rotations(chars: str) -> str:
        for i in range(len(chars)):
            yield int(chars[i:] + chars[:i])

    if not n_is_prime: return False
    for r in rotations(str(n)):
        if not is_prime(r): return False
    return True


def solution(N=1000000):
    """
    Возвращает количество круговых простых чисел меньше миллиона.

    >>> solution()
    55
    """
    sieve_bit_array = bit_sieve(N)
    return sum(1 for n in range(3, N, 2) if is_circular_prime(n, sieve_bit_array[n])) + 1
```
```
  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
  1    1.508  150.800%      1000000           55
 ```