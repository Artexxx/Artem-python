# [10001-ое простое число](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/7.html)

>Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
>
>Какое число является N-ым простым числом?

``` python
solution(10001) # => 
```

## Частное решение (1)

- Проскакивая все чётные числа, ищем N-е простое число 

``` python
def is_prime(n):
    if n == 2: return True
    elif n % 2 == 0: return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0: return False
    return True


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(10001)
    104743
    """
    count_primes = 0
    index = 1
    while count_primes != n and index < 3:
        index += 1
        if is_prime(index):
            count_primes += 1
    while count_primes != n:
        index += 2
        if is_prime(index):
            count_primes += 1
    return index
```
```text
  №       Время  Замедление      Аргумент    Результат
---  ----------  ------------  ----------  -----------
  1   0.0920908  9.209%             10001       104743 (ответ)
  2   2.86101    276.891%          100001      1299721
  3  92.5656     8970.461%        1000001     15485867
```


## Частное решение (2)

- В основе лежит *решето эратосфена* 
- N-ое простое не превосходит `1.5 * n * math.log(N)`

<img src="https://i.imgur.com/xGbfnpP.gif" alt="Eratosfen gif">


```python
def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, Return boolean array of length N, where prime indices are True.
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    Time-Profile
    ============
      №       Time  Slowdown      Argument    Count primes
    ---  ---------  ------------  ----------  ------------
      1  0.0011774  0.118%           100_000          9592
      2  0.013186   1.201%         1_000_000         78498
      3  0.131736   11.855%       10_000_000        664579
      4  1.63013    149.840%     100_000_000       5761455
    """
    sieve = bytearray([True]) * limit
    zero = bytearray([False])

    sieve[0] = False
    sieve[1] = False
    number_of_multiples = len(sieve[4::2]) # old code ─ slow version
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            number_of_multiples = len(sieve[factor * factor::2*factor])
            sieve[factor * factor::factor * 2] = zero * number_of_multiples
    return sieve


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(10001)
    104743
    """
    # N-ое простое не превосходит 1,5 N ln( N ) при N > 1:
    sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)

    count_primes = 0
    index = 1
    while count_primes != n and index < 3:
        index += 1
        if sieve[index]:
            count_primes += 1
    while count_primes != n:
        index += 2
        if sieve[index]:
            count_primes += 1
    return index
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0153429  1.534%             10001       104743 (ответ)
  2  0.254947   23.960%           100001      1299721
  3  3.19012    293.517%         1000001     15485867
```