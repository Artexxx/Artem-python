# [10001-ое простое число](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/7.html)

>Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
>
>Какое число является N-ым простым числом?

``` python
solution(6) # => 13
solution(1) # => 2
solution(3) # => 5
solution(20) # => 71
solution(50) # => 229
solution(100) # => 541

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
    count_primes = 0
    index = 1
    while count_primes != n and j < 3:
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
  №     Время  Замедление      Число    Результат
---  --------  ------------  -------  -----------
  1  0.246657  24.666%         20000       224737
  2  0.694757  44.81%          40000       479909
  3  1.95447   125.97%         80000      1020379
  4  3.67302   171.85%        120000      1583539
```


## Частное решение (2)

- В основе лежит *решето эратосфена* 
1.5 * n * math.log(n)
- N-ое простое не превосходит `1.5 * n * math.log(N)` при `N > 1`

<img src="https://i.imgur.com/xGbfnpP.gif" alt="Eratosfen gif">

```python
def bit_sieve(n):
    '''
    Решето Эратосфена. В списке bits сбрасываются биты,
    имеющие составные номера, биты с простыми номерами == 1.
    i-му по порядку элементу будет соответствовать 1, если
    i -- простое и 0 иначе. Сложность: nloglog(n).
    '''
    bits = [1] * (n + 1)
    for index in range(2, int(math.sqrt(n))):
        if bits[index]:  # если i -- простое
            for j in range(index*index, n + 1, index):  # занулить все ему кратные
                bits[j] = 0
    return bits


def solution(n):
    # N-ое простое не превосходит 1,5 N ln( N ) при N > 1:
    sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)
    index = 0
    while n:
        n -= sieve[index]
        index += 1
    return index + 1

```
```text
  №     Время  Замедление      Число    Результат
---  --------  ------------  -------  -----------
  1  0.652925  65.293%        200000      2750125
  2  0.99529   34.24%         300000      4256193
  3  1.36281   36.75%         400000      5800051
  4  2.15794   79.51%         600000      8960445
```