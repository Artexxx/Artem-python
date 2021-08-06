# [Наименьшее кратное](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/4.html)

> `2520` - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
>
> Какое самое маленькое число делится нацело на все числа от 1 до N?

``` python
solution(10) # => 2520
solution(15) # => 360360
solution(20) # => 232792560
solution(22) # => 232792560
```

## Нормальное решение (1)

- В основе лежит *фундаментальная арифметическая теорема* 
    - смотри 3 Решение

``` python
def primes_mutiples_until(end):
    """
    Разделяет все числа от [1 до end] на простые и составные.
    >>> primes_mutiples_until(8)
    ([2, 3, 5, 7], [4, 6, 8])
    """
    primes, multiples = [], []
    for i in range(2, end + 1):
        if is_prime(i):
            primes.append(i)
        else:
            multiples.append(i)
    return primes, multiples


def solution(end):
    the_number = 1
    primes, multiples = primes_mutiples_until(end)

    for p in primes: the_number *= p

    for m in multiples:
        reminder = the_number % m
        if reminder != 0:
            if is_prime(reminder):
                the_number *= reminder
            else:
                for p in primes:
                    if reminder % p == 0:
                        the_number *= p
                        break
    return the_number

```
```text
  №     Время  Замедление      Число                                   Результат
---  --------  ------------  -------  ------------------------------------------
  1  9.6e-06   0.001%             10                                        2520
  2  1.04e-05  0.00%              15                                      240240
  3  1.37e-05  0.00%              20                                   232792560
  4  1.83e-05  0.00%              25                                  7138971840
  5  4.16e-05  0.00%              50                       354176514770971052160
  6  7.13e-05  0.00%             100  793262935946950851294251337219553320468480
```


## Нормальное решение (2)

- В основе лежит *фундаментальная арифметическая теорема* 

1. Находим простые чисела, образующие х, где x - это число от 2 до N
2. Разделяем подряд идущие простые числа на частоты
    <br> Пример: [2, 2, 3, 3, 2, 3] ~>  [2, 2], [3, 2], [2, 1], [3, 1]
3. Для каждого числа нажодим максимальную частоту
    <br> Пример: [2, 2],  [3, 2],  [2, 1],  [3, 1] ~>  { 2: 2, 3: 2 }

``` python
import math

def prime_factors(x) -> list:
    """ Возвращает простые чисела, образующие х

    >>> prime_factors(24)
    [2, 2, 2, 3]
    """
    if x <= 1: return []
    for i in range(2, x + 1):
        if x % i == 0:
            return [i, *prime_factors(x // i)]


def primes_frequency(primes: list) -> list:
    """"Возвращает частоты последовательных простых чисел

    >>> primes_frequency([2, 2, 3, 3, 2, 3])
    [[2, 2], [3, 2], [2, 1], [3, 1]]
    """
    frequency = [[primes[0], 1]]

    for i in range(1, len(primes)):
        if primes[i] != primes[i - 1]:
            frequency.append([primes[i], 1])
        else:
            frequency[-1][1] += 1
    return frequency


def primes_greatest_frequency(primes_frequency_list: list) -> dict:
    """Возвращает самые большие частоты последовательных простых чисел

    >>> primes_greatest_frequency([2, 2])
    { 2: 2, 3: 2 }
    """
    max_frequency = {}
    for frequency in primes_frequency_list:
        value = max_frequency.get(frequency[0])
        if value:
            max_frequency[frequency[0]] = max(value, frequency[1])
        else:
            max_frequency[frequency[0]] = frequency[1]
    return max_frequency


def solution(n):
    """Возвращает наименьшее положительное число, которое равномерно делится (без остатка) на все числа от 1 до n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    """
    primes = []
    for i in range(n, 1, -1):
        primes.extend(prime_factors(i))
    primes_frequency_list = primes_frequency(primes)
    max_frequency = primes_greatest_frequency(primes_frequency_list)

    result_number = 1
    for item in max_frequency.items():
        result_number *= math.pow(*item)
    return result_number
```
```text
  №     Время  Замедление      Число                                   Результат
---  --------  ------------  -------  ------------------------------------------
  1  1.04e-05  0.001%             10                                        2520
  2  2.04e-05  0.00%              15                                      240240
  3  2.37e-05  0.00%              20                                   232792560
  4  2.83e-05  0.00%              25                                  7138971840
  5  3.16e-05  0.00%              50                       354176514770971052160
  6  3.13e-05  0.00%             100  793262935946950851294251337219553320468480
```


## Нормальное решение (3)

Наименьшее число n, которое равномерно делится (без остатка) на каждое число в множестве {k1, k2,..., к_m},
также известено как наименьшее общее кратное (НОК) из множества чисел.
 
LCM двух натуральных чисел x и y получается так: НОК(x, y) = x * y / НОД(x, y).
Когда НОК применяется к набору чисел, он является коммутативным, ассоциативным и идемпотентным.
Следовательно, НОК(k1, k2,..., k_m) = НОК(...(НОК(НОК (k1, k2), k3)...), k_m).

```python

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return (x * y) // gcd(x, y)


def solution(n):
    g = 1
    for i in range(1, n + 1):
        g = lcm(g, i)
    return g
```
```text
  №     Время  Замедление      Число                                   Результат
---  --------  ------------  -------  ------------------------------------------
  1  9.6e-06   0.001%             10                                        2520
  2  1.04e-05  0.00%              15                                      240240
  3  1.37e-05  0.00%              20                                   232792560
  4  1.83e-05  0.00%              25                                  7138971840
  5  4.16e-05  0.00%              50                       354176514770971052160
  6  7.13e-05  0.00%             100  793262935946950851294251337219553320468480
```