# [Сложение простых чисел](https://www.codewars.com/kata/59ab0ca4243eae9fec000088/train/python)

## [Проблема](https://euler.jakumo.org/problems/view/10.html)

>Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
>
>Найдите сумму всех простых чисел меньше `n`.

*Решение должно работать для действительно больших чисел (более 10 000 000).*


``` python
solution(7) # => 10 = 2 + 3 + 5
solution(10) # => 17 = 2 + 3 + 5 + 7
solution(10 000) # => 5736396
solution(1 000 000) # => 37550402023
solution(2 000 000) # => 142913828922
```

## Частное решение (1)

``` python
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0: return False
    return True


def solution(n):
    if n > 2:
        result_sum = 2
    else:
        return 0

    for candidate in range(3, n, 2):
        if is_prime(candidate):
            result_sum += candidate
    return result_sum
```
```text
  №       Время  Замедление        Число     Результат
---  ----------  ------------    -------  ------------
  1   0.0051545  0.515%           10_000       5736396
  2   0.0862083  8.11%           100_000     454396537
  3   1.90828    182.21%       1_000_000   37550402023
  4  18.3567     1644.84%      5_000_000  838596693108
```

## Частное решение (2)

- *Решето Эратосфена* - один из самых эффективных способов найти все простые числа меньше n, когда n меньше 10 миллионов.

<img src="https://github.com/karimelgazar/Project-Euler/blob/master/010%20Summation%20of%20primes/way.gif?raw=true" alt="Eratosfen gif 2 ">

> ### Пример для n = 30 ###
> Запишем натуральные числа, начиная от `2`, до `30` в ряд:
>
> *2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30*
>
> Первое число в списке, `2` — простое. Пройдём по ряду чисел, зачёркивая все числа, кратные 2 (то есть, каждое второе, начиная с `2*2 = 4`):
>
>*2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30*
>
>Следующее не зачеркнутое число, `3` — простое. Пройдём по ряду чисел, зачёркивая все числа, кратные 3 (то есть, каждое третье, начиная с `3*3 = 9`):
>
>*2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30*
>
>Следующее не зачеркнутое число, `5` — простое. Пройдём по ряду чисел, зачёркивая все числа, кратные 5 (то есть, каждое пятое, начиная с `5*5 = 25`):
>
>*2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30*
>
>Следующее не зачеркнутое число — `7`. Его квадрат, 49 — больше 30, поэтому на этом работа завершена. Все составные числа уже зачеркнуты:
>
>*2  3     5     7           11    13          17    19          23                29*
```python
def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, return boolean array of length `limit`,
    where index is number and boolean values is whether prime or not
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    Time-Profile
    ============
    ===  =========  ============  ===========  ============
      №       Time  Slowdown         Argument  Count primes
    ===  =========  ============  ===========  ============
      1  0.001174   0.118%            100_000          9592
      2  0.013186   1.201%          1_000_000         78498
      3  0.131736   11.855%        10_000_000        664579
      4  1.63013    149.840%      100_000_000       5761455
    ===  =========  ============  ===========  ============
    """
    sieve = bytearray([True]) * limit
    zero = bytearray([False])

    sieve[0] = False
    sieve[1] = False
    number_of_multiples = len(sieve[4::2])
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            number_of_multiples = len(sieve[factor * factor::2*factor])
            sieve[factor * factor::factor * 2] = zero * number_of_multiples
    return sieve


def solution(limit: int) -> int:
    sieve = bit_sieve(limit)
    prime_sum = 2
    for i in range(3, limit, 2):
        if sieve[i]:
            prime_sum += i
    return prime_sum
```
```text
  №      Время  Замедление      Аргумент       Результат
---  ---------  ------------  ----------  --------------
  1  0.0031426  0.314%           100_000       454396537
  2  0.0310431  2.790%         1_000_000     37550402023
  3  0.310128   27.908%       10_000_000   3203324994356
  4  1.72953    141.940%      50_000_000  72619548630277
```
