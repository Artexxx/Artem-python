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
def bit_sieve(n) -> list:
    """
    Решето Эратосфена.
    Сложность: nloglog(n).
    """
    bits = [True] * (n + 1)
    for index in range(2, int(math.sqrt(n))):
        if bits[index]:  # если i - простое
            for j in range(index * index, n + 1, index):  # занулить все ему кратные
                bits[j] = False
    return bits


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