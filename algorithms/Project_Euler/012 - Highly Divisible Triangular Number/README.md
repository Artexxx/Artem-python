# [Треугольное число с большим количеством делителей](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/12.html)

>Последовательность треугольных чисел образуется путем сложения натуральных чисел.
> К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
>
>Первые десять треугольных чисел:
>
>1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
>
>Перечислим делители первых семи треугольных чисел:
>
> **1**: 1
>
> **3**: 1, 3
>
> **6**: 1, 2, 3, 6
>
> **10**: 1, 2, 5, 10
>
> **15**: 1, 3, 5, 15
>
> **21**: 1, 3, 7, 21
>
> **28**: 1, 2, 4, 7, 14, 28
>
>Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
>
>Каково первое треугольное число, у которого более N делителей?


``` python
solution (5) # => 28 = 1, 2, 4, 7, 14, 28
solution (500) # => 76576500
```

## Частное решение (1)

```python
def triangle_number_generator():
    for n in itertools.count(1):
        yield n * (n + 1) // 2

# Old Method!!!
# def count_divisors(n): 
#     count = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             count += 1
#             if n / i != i:
#               count += 1
#     return count


def count_divisors(n):
    return sum([2 for i in range(1, int(math.sqrt(n)) + 1)
                if n % i == 0 and i * i != n])


def solution(n):
    return next(i for i in triangle_number_generator() if count_divisors(i) > n)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0010739  0.107%             50        25200
  2  0.0889911  8.79%             250      2162160
  3  2.97749    288.85%           500     76576500
```


## Частное решение (2)

***Факторизация*** - это тяжёлая задача. Начиная с `n * (n + 1) / 2` я брал трудную проблему и усложнял её.
Гораздо легче разложить `7 * 4`, чем 28.

```python
def memoize(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[#] F(",int(*args), ')\t => \t', dict(cache[args])) # TEST OUTPUT
        return cache[args]
    return wrapper


@memoize
def prime_factorization(x):
    for i in range(2, math.floor(math.sqrt(x) + 1)):
        if x % i == 0:
            old_factorization = prime_factorization(x / i).copy()
            old_factorization[i] += 1
            return old_factorization
    # Нет делителей -> x простое число
    res = collections.defaultdict(int)
    res[x] = 1
    return res


def merge_factors(f1, f2):
    res = f1.copy()
    for k, v in f2.items():
        res[k] += v
    return res


def num_factors(factorization):
    product = 1
    for v in factorization.values():
        product *= (v + 1)
    return product


def solution(N):
    for n in itertools.count(start=1):
        factors1 = prime_factorization(n / 2 if n % 2 == 0 else n)
        factors2 = prime_factorization(n + 1 if n % 2 == 0 else (n + 1) / 2)
        full_factorization = merge_factors(factors1, factors2)

        if num_factors(full_factorization) >= N:
            print("The first triangular number with {} divisors is {:,}".format(N, n * (n + 1) / 2))
            return int(n * (n + 1) / 2
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0006367  0.064%             50        25200
  2  0.0139099  1.33%             250      2162160
  3  0.220611   20.67%            500     76576500
  4  1.44833    122.77%          1000    842161320
  5  8.62281    717.45%          1500   7589181600
```