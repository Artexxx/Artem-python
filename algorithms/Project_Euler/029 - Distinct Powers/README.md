# [Различные степени](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/29.html)

> Рассмотрим все целочисленные комбинации <i>a</i><sup><i>b</i></sup> для `2 ≤ a ≤ 5` и `2 ≤ b ≤ 5`:
>
>2<sup>2</sup>=4, 2<sup>3</sup>=8, 2<sup>4</sup>=16, 2<sup>5</sup>=32<br>
3<sup>2</sup>=9, 3<sup>3</sup>=27, 3<sup>4</sup>=81, 3<sup>5</sup>=243<br>
4<sup>2</sup>=16, 4<sup>3</sup>=64, 4<sup>4</sup>=256, 4<sup>5</sup>=1024<br>
5<sup>2</sup>=25, 5<sup>3</sup>=125, 5<sup>4</sup>=625, 5<sup>5</sup>=3125<br>
>
>Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность из 15 различных членов:
>
> 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
>
>Сколько различных членов имеет последовательность <i>a</i><sup><i>b</i></sup> для `2 ≤ a ≤ n` и `2 ≤ b ≤ n`?
>

``` python
solution   (3)  # => 4 = 4 ,8, 9, 27
solution   (5)  # => 15 = 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
solution   (1000)  # => 977_358
```



## Частное решение (1)

```python
def solution(n):
    collectPowers = set()
    currentPow = 0

    N = n + 1
    for a in range(2, N):
        for b in range(2, N):
            currentPow = a ** b  # вычисляет текущую степень
            collectPowers.add(currentPow)  # добавлеям результат в множество
    return len(collectPowers)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  3.96e-05   0.004%             10           69
  2  0.0090382  0.90%             100         9183
  3  6.30244    629.34%          1000       977358
```
## Нормальное решение (1)

```python
def distinctProducts(n, m):
    """
    Возрощает количество различных произведений a и b для  1<=a<=n и 2<=b<=m
    >>> distinctProducts(1, 5)
    4
    >>> distinctProducts(2, 5)
    7   # 1:(2, 3, 4, 5) 2:({2}, {4}, 6, 8, 10)

    """
    set_products = set()

    for a in range(1, n + 1):
        for b in range(2, m + 1):
            set_products.add(a * b)
    return len(set_products)


def distinctPowers(n):
    imperfect_powers = [True] * (n + 1)
    root = int(n ** 0.5)
    n_distinct = checked = 0
    for a in range(2, root + 1):
        if imperfect_powers[a]:
            max_power = 1
            a_pow = a ** 2
            while a_pow <= n:
                imperfect_powers[a_pow] = False
                max_power += 1
                a_pow *= a
            n_distinct += distinctProducts(max_power, n)
            checked += max_power
    n_distinct += (n - 1) * (n - checked - 1)
    return n_distinct
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0054298  0.543%           1000       977358
  2  0.182178   17.67%         10_000     99347607
  3  5.86805    568.59%       100_000   9981236306
```