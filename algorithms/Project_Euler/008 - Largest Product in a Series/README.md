# [Наибольшее произведение в последовательности](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/8.html)

>Наибольшее произведение четырех последовательных цифр в 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
>
>Найдите наибольшее произведение N последовательных цифр в данном числе.

``` python
solution(4) # => 5832 = 9 × 9 × 8 × 9
solution(5) # => 40824 = 9 * 9 * 8 * 7 * 9
```

## Частное решение (1)

``` python
def solution(n: int, NUMBER: str = DEFAULT_NUMBER):
    LargestProduct = -sys.maxsize
    for i in range(len(NUMBER) - n):
        product = 1
        for j in range(n):
            product *= int(NUMBER[i + j])
        if product > LargestProduct:
            LargestProduct = product
    return LargestProduct
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  1.61e-05   0.002%             12           60
  2  0.0823076  8.23%             234       453960
  3  5.93164    584.93%          1000     31875000
```


## Частное решение (2)

```python
from functools import reduce
def solution(n: int, NUMBER: str = DEFAULT_NUMBER):
    return max(
        [
            reduce(lambda x, y: int(x) * int(y), NUMBER[i : i + n])
            for i in range(len(NUMBER) - (n-1))
        ]
    )
```
```text
  №      Время  Замедление      Число              Результат
---  ---------  ------------  -------  ---------------------
  1  0.0009721  0.097%              4                   5832
  2  0.0022933  0.13%              10              493807104
  3  0.0041086  0.18%              20        240789749760000
  4  0.0068901  0.28%              30  374476218826752000000
```