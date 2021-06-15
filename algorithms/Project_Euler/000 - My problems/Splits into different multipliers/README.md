**Задача:**
<br>
Дано натуральное число N.
Требуется найти число способов представить его в виде произведения попарно различных множителей больших 1.

**Формат входных данных**

N — натуральное число `2<=N<=10**12`.
 
**Формат выходных данных**

Вывести одно число - количество способов представить число N в виде произведения попарно различных множителей больших 1.


**Пояснение к примеру.**

Имеется 7 различных способов представить число 48 в виде произведения (в том числе и вырожденного) попарно различных множителей больших 1:
`48, 2*24, 3*16, 4*12, 6*8, 2*3*8, 2*4*6`. 

**Пример запуска программы:**
<br>
```python
>>> count_factors_comb(48)
7 ###  [[2, 3, 8], [2, 4, 6], [2, 24], [3, 16], [4, 12], [6, 8], [48]] ###
```

```python
>>> count_factors_comb(24)
5 ###   [[2, 3, 4], [2, 12], [3, 8], [4, 6], [1, 24]] ###
```
```python
>>> count_factors_comb(12)
3 ###   [[2, 6], [3, 4], [1, 12]]  ###
```

## Нормальное решение (1)
```python
def get_custom_factorization(N, min_lim_factor):
    """
    Возвращает множители числа N в пределе [min_lim_factor: sqrt(N)]

    >>> get_custom_factorization(48, min_lim_factor=4)
    [4, 6, 48] # нет 2 и 3
    """
    result_factors = []
    i = 1
    while i * i <= N:
        if N % i == 0 and i >= min_lim_factor:
            result_factors.append(i)
        i += 1
    result_factors.append(N)
    return result_factors


def get_factors_comb(n, min_factor, _list_of_factors, result_list_of_factors):
    if n == 1:
        # получатся из n // factor, означает что мы нашли 1 разложение на множители
        result_list_of_factors.append(_list_of_factors)
    else:
        for factor in get_custom_factorization(n, min_factor):
            if factor not in _list_of_factors:
                factors_pair(n=n // factor,
                             min_factor=factor + 1,
                             _list_of_factors=_list_of_factors + [factor],
                             result_list_of_factors=result_list_of_factors)
                if n == factor:
                    return result_list_of_factors


_list_of_factors = get_factors_comb(48, 2, [], [])
print(len(_list_of_factors))
```
```text
  №      Время  Замедление            Число    Результат
---  ---------  ------------  -------------  -----------
  1  0.0028411  0.284%              1000000          323
  2  0.0386391  3.58%             100000000         1966
  3  0.476018   43.74%          10000000000        10792
  4  6.43207    595.61%       1000000000000        54344
```


```python
from functools import lru_cache

@lru_cache(maxsize=None)
def count_factors_comb_opt(n, min_factor=2):
    return n >= min_factor and \
           1 + sum(count_factors_comb_opt(n//temp_factor, temp_factor+1)
           for temp_factor in range(min_factor, int(n**.5)+1)
                if n % temp_factor == 0)
```
