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
def bit_sieve(n) -> list:
    """ Sieve of Eratosthenes
     Generate boolean array of length N, where prime indices are True.

    The time complexity of this algorithm is O(nloglog(n).

    >>> bit_sieve(10)
    [False, False, True, True, False, True, False, True, False, False]
    """
    primes = [True] * n
    primes[0], primes[1] = False, False  # числа 0 и 1

    number_of_multiples = len(primes[4::2])
    primes[4::2] = [False] * number_of_multiples
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[factor]:
            number_of_multiples = len(primes[factor * factor::factor * 2])
            primes[factor * factor::factor * 2] = [False] * number_of_multiples
    return primes


PRIMES = bit_sieve(10 ** 6)


def is_circular_prime(n: int) -> bool:
    def rotations(chars: str) -> int:
        for i in range(len(chars)):
            yield int(chars[i:] + chars[:i])

    str_n = str(n)
    # Многозначное простое число не может оканчиваться четными цифрами 0, 2, 4, 6, 8, и цифрой 5
    if '5' in str_n or '0' in str_n or '2' in str_n or '4' in str_n or '6' in str_n or '8' in str_n:
        return False
    
    for r in rotations(str_n):
        if not PRIMES[r]: return False
    return True


def solution():
    """
    Возвращает количество круговых простых чисел меньше миллиона.

    >>> solution()
    55
    """
    return sum(1 for n in range(101, 10 ** 6, 2)
               if PRIMES[n] and is_circular_prime(n)) + 13
```
```
   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  -----------
0.126704  12.670%       1000000              55
 ```